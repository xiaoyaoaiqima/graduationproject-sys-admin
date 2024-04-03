from rest_framework.views import APIView
from business.models import *
from system.models import *
from django.db import connection
from system.utils.json_response import *
from rest_framework import status
from django.core.paginator import Paginator
from system.utils.user import UserToken



# 用户
class UserListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = User.objects.all()
            serializerList = UserSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = User.objects.get(id=pk)
            serializer = UserSerializer(model)
            return SuccessResponse(data=serializer.data)

class UserPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = User.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = UserSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )
								
# 网站公告
class NoticeListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Notice.objects.all()
            serializerList = NoticeSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Notice.objects.get(id=pk)
            serializer = NoticeSerializer(model)
            return SuccessResponse(data=serializer.data)

class NoticePage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Notice.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = NoticeSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )

								
# 根据userId查询用户
class getStudentByUserId(APIView):
    def get(self, request, userId):
        model = Student.objects.filter(user_id=userId).first()
        serializer = StudentSerializer(model)
        return SuccessResponse(data=serializer.data)

class UpdateStudent(APIView):
    # 新增/修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = StudentSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")

        try:
            model = Student.objects.get(pk=request.data['id'])
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")
# 根据userId查询教师
class getTeacherByUserId(APIView):
    def get(self, request, userId):
        model = Teacher.objects.filter(user_id=userId).first()
        serializer = TeacherSerializer(model)
        return SuccessResponse(data=serializer.data)

class UpdateTeacher(APIView):
    # 新增/修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = TeacherSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")

        try:
            model = Teacher.objects.get(pk=request.data['id'])
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 宣传图
class BannerListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Banner.objects.all()
            serializerList = BannerSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Banner.objects.get(id=pk)
            serializer = BannerSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Banner.objects.get(pk=request.data['id'])
        except Banner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Banner.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class BannerPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Banner.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = BannerSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateBanner(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = BannerSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Banner.objects.get(pk=request.data['id'])
        except Banner.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 用户
class StudentListDetail(APIView):
    # 列表和查询一个
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
        serializer = StudentSerializer(data=request.data)
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
		
class StudentPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Student.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

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


class UpdateStudent(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = StudentSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Student.objects.get(pk=request.data['id'])
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 教师
class TeacherListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Teacher.objects.all()
            serializerList = TeacherSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Teacher.objects.get(id=pk)
            serializer = TeacherSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Teacher.objects.get(pk=request.data['id'])
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Teacher.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class TeacherPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Teacher.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = TeacherSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateTeacher(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = TeacherSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Teacher.objects.get(pk=request.data['id'])
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 毕设选题指导
class NewsListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = News.objects.all()
            serializerList = NewsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = News.objects.get(id=pk)
            serializer = NewsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = News.objects.get(pk=request.data['id'])
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = News.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class NewsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = News.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = NewsSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateNews(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = NewsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = News.objects.get(pk=request.data['id'])
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 毕设题目分类
class CategoryListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Category.objects.all()
            serializerList = CategorySerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Category.objects.get(id=pk)
            serializer = CategorySerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Category.objects.get(pk=request.data['id'])
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Category.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class CategoryPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Category.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = CategorySerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateCategory(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = CategorySerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Category.objects.get(pk=request.data['id'])
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 毕业选题列表
class TopicsListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Topics.objects.all()
            serializerList = TopicsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Topics.objects.get(id=pk)
            serializer = TopicsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = TopicsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Topics.objects.get(pk=request.data['id'])
        except Topics.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TopicsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Topics.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class TopicsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))
        category_id = request.query_params.get('category_id')

        # 构建查询
        list = Topics.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)
        if category_id:
            list = list.filter(category_id=category_id)

        # 个性化标签推荐
        # 查询当前用户设置的标签
        user_id = UserToken.user_id(request)
        user_tags = Membertags.objects.filter(user_id=user_id).values_list("tags_id", flat=True)

        if user_tags is not None:
            # 查询包含标签的选题
            topics_id_list = Topicstags.objects.filter(tags_id__in=user_tags).values_list("topics_id", flat=True)
            list = list.filter(id__in=topics_id_list)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = TopicsSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateTopics(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = TopicsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Topics.objects.get(pk=request.data['id'])
        except Topics.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TopicsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 待选题记录
class PrerecordListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Prerecord.objects.all()
            serializerList = PrerecordSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Prerecord.objects.get(id=pk)
            serializer = PrerecordSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = PrerecordSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Prerecord.objects.get(pk=request.data['id'])
        except Prerecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PrerecordSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Prerecord.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class PrerecordPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Prerecord.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = PrerecordSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdatePrerecord(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = PrerecordSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Prerecord.objects.get(pk=request.data['id'])
        except Prerecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PrerecordSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 毕设选题记录
class RecordsListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Records.objects.all()
            serializerList = RecordsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Records.objects.get(id=pk)
            serializer = RecordsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = RecordsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Records.objects.get(pk=request.data['id'])
        except Records.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecordsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Records.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class RecordsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Records.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = RecordsSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateRecords(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = RecordsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Records.objects.get(pk=request.data['id'])
        except Records.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecordsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 私聊信息
class PmListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Pm.objects.all()
            serializerList = PmSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Pm.objects.get(id=pk)
            serializer = PmSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = PmSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Pm.objects.get(pk=request.data['id'])
        except Pm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PmSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Pm.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class PmPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Pm.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = PmSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdatePm(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = PmSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Pm.objects.get(pk=request.data['id'])
        except Pm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PmSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 题目标签
class TagsListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Tags.objects.all()
            serializerList = TagsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Tags.objects.get(id=pk)
            serializer = TagsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = TagsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Tags.objects.get(pk=request.data['id'])
        except Tags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TagsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Tags.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class TagsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Tags.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = TagsSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateTags(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = TagsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Tags.objects.get(pk=request.data['id'])
        except Tags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TagsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 我的选题标签
class MembertagsListDetail(APIView):
    # 列表和查询一个
    def get(self, request , pk=None):
        if pk is None:
            list = Membertags.objects.all()
            serializerList = MembertagsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Membertags.objects.get(id=pk)
            serializer = MembertagsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = MembertagsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Membertags.objects.get(pk=request.data['id'])
        except Membertags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MembertagsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Membertags.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")
		
class MembertagsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Membertags.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = MembertagsSerializer(pageList,many=True)
        return PageResponse(page=pageNum,
                                limit=pageSize,
                                total=paginator.count,
                                pages=paginator.num_pages,
                                data=serializerList.data
                                )


class UpdateMembertags(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = MembertagsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Membertags.objects.get(pk=request.data['id'])
        except Membertags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MembertagsSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.update(model,serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")


# 选题关联标签
class TopicstagsListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Topicstags.objects.all()
            serializerList = TopicstagsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Topicstags.objects.get(id=pk)
            serializer = TopicstagsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = TopicstagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Topicstags.objects.get(pk=request.data['id'])
        except Topicstags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TopicstagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Topicstags.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class TopicstagsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Topicstags.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = TopicstagsSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )

# 根据选题ID查询标签列表
class GetTagsByTopicId(APIView):
    # 列表和查询一个
    def get(self, request, topicsId=None):
        model = Topicstags.objects.filter(topics_id=topicsId).values_list('tags_id', flat=True)
        data = list(model)
        return SuccessResponse(data=data)

# 根据选题ID删除标签列表
class DelTagsByTopicId(APIView):
    # 列表和查询一个
    def delete(self, request, topicsId=None):
        model = Topicstags.objects.filter(topics_id=topicsId).all()
        model.delete()
        return SuccessResponse(msg="删除成功")

class UpdateTopicstags(APIView):
    # 修改
    def put(self, request):
        if 'id' not in request.data:
            # 新增
            serializer = TopicstagsSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return SuccessResponse(msg="添加成功")
            else:
                return ErrorResponse(msg="数据验证失败")
        try:
            model = Topicstags.objects.get(pk=request.data['id'])
        except Topicstags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TopicstagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

# 添加/修改购物车
class UpdatePrerecord(APIView):
    def post(self, request):
        id = None
        if 'id' in request.data:
            id = request.data['id']
        name = None
        if 'name' in request.data:
            name = request.data['name']
        num = None
        if 'num' in request.data:
            num = request.data['num']
        img = None
        if 'img' in request.data:
            img = request.data['img']
        price = None
        if 'price' in request.data:
            price = request.data['price']
        userId = None
        if 'userId' in request.data:
            userId = request.data['userId']
        if 'goodid' in request.data:
            goodid = request.data['goodid']
        bizUserId = None
        if 'bizUserId' in request.data:
            bizUserId = request.data['bizUserId']

        # 判断学生是否已经选题
        count = Records.objects.filter(state_radio__in=['提交申请','审核通过'],user_id=userId).count()
        if count>0:
            return ErrorResponse(msg="你已经选过题目，请勿重复选择")

        cart = Prerecord.objects.filter(name=name,user_id=userId).first()
        if cart:
            if id:
                cart.num = num
                cart.save()
            else:
                cart.num = cart.num+num
                cart.save()
            return SuccessResponse(msg="操作成功")
        else:
            Prerecord.objects.create(
                name=name,
                user_id=userId,
                goodid=goodid,
                biz_user_id=bizUserId
            )
            return SuccessResponse(msg="添加成功")


# 选题关联标签
class TopicstagsListDetail(APIView):
    # 列表和查询一个
    def get(self, request, pk=None):
        if pk is None:
            list = Topicstags.objects.all()
            serializerList = TopicstagsSerializer(list, many=True)
            return SuccessResponse(data=serializerList.data)
        else:
            model = Topicstags.objects.get(id=pk)
            serializer = TopicstagsSerializer(model)
            return SuccessResponse(data=serializer.data)

    # 新增
    def post(self, request):
        serializer = TopicstagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return SuccessResponse(msg="添加成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 修改
    def put(self, request):
        try:
            model = Topicstags.objects.get(pk=request.data['id'])
        except Topicstags.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TopicstagsSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.update(model, serializer.validated_data)
            return SuccessResponse(msg="修改成功")
        else:
            return ErrorResponse(msg="数据验证失败")

    # 删除
    def delete(self, request, pk):
        model = Topicstags.objects.filter(id=pk)
        model.delete()
        return SuccessResponse(msg="删除成功")


class TopicstagsPage(APIView):

    # 分页
    def get(self, request):
        name = request.query_params.get('name')
        pageNum = int(request.query_params.get('pageNum', 1))
        pageSize = int(request.query_params.get('pageSize', 5))

        # 构建查询
        list = Topicstags.objects.all().order_by('-id')
        if name:
            list = list.filter(name__icontains=name)

        # 进行分页
        paginator = Paginator(list, pageSize)
        pageList = paginator.page(pageNum)
        serializerList = TopicstagsSerializer(pageList, many=True)
        return PageResponse(page=pageNum,
                            limit=pageSize,
                            total=paginator.count,
                            pages=paginator.num_pages,
                            data=serializerList.data
                            )


# 添加/修改订单
class UpdateRecords(APIView):
    def post(self, request):
        id = None
        if 'id' in request.data:
            id = request.data['id']
        name = None
        if 'name' in request.data:
            name = request.data['name']
        content = None
        if 'content' in request.data:
            content = request.data['content']
        stateRadio = None
        if 'stateRadio' in request.data:
            stateRadio = request.data['stateRadio']
        userId = None
        if 'userId' in request.data:
            userId = request.data['userId']
        amount = None
        if 'amount' in request.data:
            amount = request.data['amount']
        goodids = None
        if 'goodids' in request.data:
            goodids = request.data['goodids']
        bizUserId = None
        if 'bizUserId' in request.data:
            bizUserId = request.data['bizUserId']

        if id:
            dbOrders = Records.objects.filter(id=id).first()
            if dbOrders:
                if name is not None:
                    dbOrders.name=name
                if content is not None:
                    dbOrders.content=content
                if stateRadio is not None:
                    dbOrders.state_radio=stateRadio
                if userId is not None:
                    dbOrders.user_id=userId
                if amount is not None:
                    dbOrders.amount=amount
                if goodids is not None:
                    dbOrders.goodids=goodids
                dbOrders.save()
        else:
            Records.objects.create(
            name=name,
            content=content,
            state_radio=stateRadio,
            user_id=userId,
            goodids=goodids,
            biz_user_id=bizUserId,
            )
        return SuccessResponse(msg="操作成功")

# 取消订单
class CancelRecords(APIView):
    def put(self, request, pk):
        curAddr = Records.objects.filter(id=pk).first()
        curAddr.state_radio = '已取消'
        curAddr.save()
        return SuccessResponse(msg="取消成功")



# 统计-毕设选题分类数量
class categoryCountView(APIView):
    def get(self,request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "select count(*) as categoryCount from category"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result[0])

# 统计-毕设题目数量
class topicsCountView(APIView):
    def get(self,request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "select count(*) as topicsCount from topics"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result[0])

# 统计-学生数量
class studentCountView(APIView):
    def get(self,request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "select count(*) as studentCount from student"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result[0])

# 统计-选题记录数量
class recordsCountView(APIView):
    def get(self,request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "select count(*) as recordsCount from records"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result[0])


	
# 统计-选题分类数量统计
class topicsCategoryView(APIView):
    def get(self,request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT c.name AS `name`,COUNT(c.name) AS `value` FROM topics r INNER JOIN category c WHERE c.id = r.category_id GROUP BY c.name"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)

# 统计-毕设题目选题人数统计
class recordsStaticsView(APIView):
    def get(self,request):
        '''
        sql = "SELECT * FROM my_table WHERE id = %s AND name = %s"
        params = (0, 1)
        params = (1, "John")
        '''

        sql = "SELECT t.name AS `name`,COUNT(r.id) `value` FROM topics t INNER JOIN records r ON r.goodids=t.id GROUP BY t.name"
        params = None
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            result = []
            for row in rows:
                data = dict(zip(columns, row))
                result.append(data)
        return SuccessResponse(data=result)

		




# 添加推荐标签
class AddTags(APIView):
    # 修改
    def post(self, request, tagsId , userId):
        Membertags.objects.create(
            user_id=userId,
            tags_id=tagsId,
        )
        return SuccessResponse(msg="操作成功")
		
# 删除推荐标签
class DeleteTags(APIView):
    # 修改
    def delete(self, request, tagsId , userId):
        Membertags.objects.filter(
            user_id=userId,
            tags_id=tagsId,
        ).delete()
        return SuccessResponse(msg="操作成功")

def to_camel_case(s):
    parts = s.split('_')
    return parts[0] + ''.join(part.title() for part in parts[1:])

def convert_props_to_camel_case(data):
    for key, value in list(data.items()):
        if isinstance(value, dict):
            convert_props_to_camel_case(value)
        elif isinstance(value, list):
            for item in value:
                convert_props_to_camel_case(item)
        camel_case_key = to_camel_case(key)
        data[camel_case_key] = data.pop(key)
