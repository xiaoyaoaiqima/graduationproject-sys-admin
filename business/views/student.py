from datetime import datetime
from django.apps import apps
from django.core.paginator import Paginator
from django.http import HttpResponse
from openpyxl import Workbook
from pytz import timezone
from rest_framework import status
from rest_framework.views import APIView
from business.models import *
from system.models import *
from system.utils.json_response import *
import uuid
import hashlib
from system.utils.user import UserToken

# 用户
class StudentView(APIView):

    # 查询数据
    def get(self, request , pk=None):
        if pk is None:
            list = Student.objects.all()
            serializerList = StudentSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Student.objects.get(id=pk)
            serializer = StudentSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        uid = uuid.uuid1()
        password = '123'
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        hashed_password = md5.hexdigest()
        email = request.data['username']+'@qq.com'
        user = User.objects.create(username=request.data['username'],name=request.data['username'],uid=uid,password=hashed_password,role='student',email=email,address='')
        request_data = request.data.copy()
        request_data['user_id'] = user.id
        serializer = StudentSerializer(data=request_data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Student.objects.get(pk=request.data['id'])
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(pk=model.user_id)
        user.name = request.data['name']
        user.save()

        serializer = StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Student.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")

# 分页
class StudentPageView(APIView):

    # 查询数据
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        user_id = UserToken.user_id(request)
        user = User.objects.get(pk=user_id)

        # 构建查询
        list = Student.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        if user.role == 'student':
            list = list.filter(user_id=user.id)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = StudentSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )

class StudentBatchDeleteAPIView(APIView):
    def post(self, request):
        ids = request.data
        try:
            Student.objects.filter(id__in=ids).delete()
            return SuccessResponse(msg="删除成功")
        except:
            return ErrorResponse(msg="删除失败")


class StudentExport(APIView):
    model = Student
    queryset = model.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Student.xlsx"'

        # 创建Excel工作簿和工作表
        wb = Workbook()
        sheet = wb.active

        model = apps.get_model('business','Student')
        fields = model._meta.get_fields()
        fields = [field for field in fields if not field.is_relation]
        headers = [field.verbose_name for field in fields if field.concrete]
        sheet.append(headers)
        list = Student.objects.all()
        for data in list:
            sheet_data = []
            for field in fields:
                if field.concrete:
                    value = getattr(data, field.name)
                    if isinstance(value, datetime) and value.tzinfo:
                        value = value.astimezone(timezone('UTC'))
                        value = value.replace(tzinfo=None)
                    sheet_data.append(value)
            sheet.append(sheet_data)
        wb.save(response)
        return response
