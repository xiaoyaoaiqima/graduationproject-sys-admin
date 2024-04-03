from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers

# Create your models here.
# 用户
class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    username = models.CharField(max_length=255, verbose_name="登录账号 ", null=True, blank=True, help_text="登录账号")
    name = models.CharField(max_length=255, verbose_name="学生姓名 ", null=True, blank=True, help_text="学生姓名")
    user_id = models.IntegerField(verbose_name="所属用户", null=True, blank=True, help_text="所属用户")

    @property
    def userId(self):
        return self.user_id

    class Meta:
        db_table = "student"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class StudentSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id

# 教师
class Teacher(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    username = models.CharField(max_length=255, verbose_name="登录账号 ", null=True, blank=True, help_text="登录账号")
    name = models.CharField(max_length=255, verbose_name="教师姓名 ", null=True, blank=True, help_text="教师姓名")
    user_id = models.IntegerField(verbose_name="所属用户", null=True, blank=True, help_text="所属用户")

    @property
    def userId(self):
        return self.user_id

    class Meta:
        db_table = "teacher"
        verbose_name = "教师"
        verbose_name_plural = verbose_name

class TeacherSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id


# 毕设选题指导
class News(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    name = models.CharField(max_length=255, verbose_name="标题 ", null=True, blank=True, help_text="标题")
    content = models.TextField(verbose_name="内容 ",null=True, blank=True,  help_text="内容")
    img = models.CharField(max_length=255, verbose_name="封面 ", null=True, blank=True, help_text="封面")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="发布时间", verbose_name="发布时间")

    @property
    def createTime(self):
        return self.create_time

    class Meta:
        db_table = "news"
        verbose_name = "毕设选题指导"
        verbose_name_plural = verbose_name

class NewsSerializer(serializers.ModelSerializer):
    createTime = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = '__all__'

    def get_createTime(self, obj):
        return obj.create_time

# 毕设题目分类
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    name = models.CharField(max_length=255, verbose_name="分类名称 ", null=True, blank=True, help_text="分类名称")


    class Meta:
        db_table = "category"
        verbose_name = "毕设题目分类"
        verbose_name_plural = verbose_name

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# 毕设题目
class Topics(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    category_id = models.IntegerField(verbose_name="题目分类", null=True, blank=True, help_text="题目分类")
    name = models.CharField(max_length=255, verbose_name="题目名称 ", null=True, blank=True, help_text="题目名称")
    content = models.TextField(verbose_name="题目要求 ",null=True, blank=True,  help_text="题目要求")
    user_id = models.IntegerField(verbose_name="指导教师", null=True, blank=True, help_text="指导教师")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="发布时间", verbose_name="发布时间")

    @property
    def categoryId(self):
        return self.category_id
    @property
    def userId(self):
        return self.user_id
    @property
    def createTime(self):
        return self.create_time

    class Meta:
        db_table = "topics"
        verbose_name = "毕设题目"
        verbose_name_plural = verbose_name

class TopicsSerializer(serializers.ModelSerializer):
    categoryId = serializers.SerializerMethodField()
    userId = serializers.SerializerMethodField()
    createTime = serializers.SerializerMethodField()

    class Meta:
        model = Topics
        fields = '__all__'

    def get_categoryId(self, obj):
        return obj.category_id
    def get_userId(self, obj):
        return obj.user_id
    def get_createTime(self, obj):
        return obj.create_time

# 待选题记录
class Prerecord(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    name = models.CharField(max_length=255, verbose_name="选题名称 ", null=True, blank=True, help_text="选题名称")
    user_id = models.IntegerField(verbose_name="选题学生", null=True, blank=True, help_text="选题学生")
    biz_user_id = models.IntegerField(verbose_name="指导老师", null=True, blank=True, help_text="指导老师")
    goodid = models.IntegerField(verbose_name="选题编号", null=True, blank=True, help_text="选题编号")

    @property
    def userId(self):
        return self.user_id
    @property
    def bizUserId(self):
        return self.biz_user_id

    class Meta:
        db_table = "prerecord"
        verbose_name = "待选题记录"
        verbose_name_plural = verbose_name

class PrerecordSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()
    bizUserId = serializers.SerializerMethodField()

    class Meta:
        model = Prerecord
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id
    def get_bizUserId(self, obj):
        return obj.biz_user_id

# 毕设选题记录
class Records(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    name = models.CharField(max_length=255, verbose_name="记录号 ", null=True, blank=True, help_text="记录号")
    content = models.TextField(verbose_name="选题明细 ",null=True, blank=True,  help_text="选题明细")
    state_radio = models.CharField(max_length=255, verbose_name="状态,提交申请|审核通过|审核失败|已取消 ", null=True, blank=True, help_text="状态,提交申请|审核通过|审核失败|已取消")
    reason = models.CharField(max_length=255, verbose_name="失败原因 ", null=True, blank=True, help_text="失败原因")
    user_id = models.IntegerField(verbose_name="选题学生", null=True, blank=True, help_text="选题学生")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="记录时间", verbose_name="记录时间")
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="更新时间",verbose_name="更新时间")
    biz_user_id = models.IntegerField(verbose_name="指导老师", null=True, blank=True, help_text="指导老师")
    goodids = models.CharField(max_length=255, verbose_name="选题编号 ", null=True, blank=True, help_text="选题编号")

    @property
    def stateRadio(self):
        return self.state_radio
    @property
    def userId(self):
        return self.user_id
    @property
    def createTime(self):
        return self.create_time
    @property
    def updateTime(self):
        return self.update_time
    @property
    def bizUserId(self):
        return self.biz_user_id

    class Meta:
        db_table = "records"
        verbose_name = "毕设选题记录"
        verbose_name_plural = verbose_name

class RecordsSerializer(serializers.ModelSerializer):
    stateRadio = serializers.SerializerMethodField()
    userId = serializers.SerializerMethodField()
    createTime = serializers.SerializerMethodField()
    updateTime = serializers.SerializerMethodField()
    bizUserId = serializers.SerializerMethodField()

    class Meta:
        model = Records
        fields = '__all__'

    def get_stateRadio(self, obj):
        return obj.state_radio
    def get_userId(self, obj):
        return obj.user_id
    def get_createTime(self, obj):
        return obj.create_time
    def get_updateTime(self, obj):
        return obj.update_time
    def get_bizUserId(self, obj):
        return obj.biz_user_id

# 私聊信息
class Pm(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    from_id = models.IntegerField(verbose_name="发送者", null=True, blank=True, help_text="发送者")
    to_id = models.IntegerField(verbose_name="接收者", null=True, blank=True, help_text="接收者")
    content = models.CharField(max_length=255, verbose_name="聊天内容 ", null=True, blank=True, help_text="聊天内容")
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="发送时间", verbose_name="发送时间")

    @property
    def fromId(self):
        return self.from_id
    @property
    def toId(self):
        return self.to_id
    @property
    def createTime(self):
        return self.create_time

    class Meta:
        db_table = "pm"
        verbose_name = "私聊信息"
        verbose_name_plural = verbose_name

class PmSerializer(serializers.ModelSerializer):
    fromId = serializers.SerializerMethodField()
    toId = serializers.SerializerMethodField()
    createTime = serializers.SerializerMethodField()

    class Meta:
        model = Pm
        fields = '__all__'

    def get_fromId(self, obj):
        return obj.from_id
    def get_toId(self, obj):
        return obj.to_id
    def get_createTime(self, obj):
        return obj.create_time

# 题目标签
class Tags(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    name = models.CharField(max_length=255, verbose_name="标签名称 ", null=True, blank=True, help_text="标签名称")


    class Meta:
        db_table = "tags"
        verbose_name = "题目标签"
        verbose_name_plural = verbose_name

class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'


# 用户标签
class Membertags(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    user_id = models.IntegerField(verbose_name="用户编号", null=True, blank=True, help_text="用户编号")
    tags_id = models.IntegerField(verbose_name="标签编号", null=True, blank=True, help_text="标签编号")

    @property
    def userId(self):
        return self.user_id
    @property
    def tagsId(self):
        return self.tags_id

    class Meta:
        db_table = "membertags"
        verbose_name = "用户标签"
        verbose_name_plural = verbose_name

class MembertagsSerializer(serializers.ModelSerializer):
    userId = serializers.SerializerMethodField()
    tagsId = serializers.SerializerMethodField()

    class Meta:
        model = Membertags
        fields = '__all__'

    def get_userId(self, obj):
        return obj.user_id
    def get_tagsId(self, obj):
        return obj.tags_id


# 选题关联标签
class Topicstags(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="编号", help_text="编号")
    topics_id = models.IntegerField(verbose_name="选题编号", null=True, blank=True, help_text="选题编号")
    tags_id = models.IntegerField(verbose_name="标签编号", null=True, blank=True, help_text="标签编号")

    @property
    def topicsId(self):
        return self.topics_id
    @property
    def tagsId(self):
        return self.tags_id

    class Meta:
        db_table = "topicstags"
        verbose_name = "选题关联标签"
        verbose_name_plural = verbose_name

class TopicstagsSerializer(serializers.ModelSerializer):
    topicsId = serializers.SerializerMethodField()
    tagsId = serializers.SerializerMethodField()

    class Meta:
        model = Topicstags
        fields = '__all__'

    def get_topicsId(self, obj):
        return obj.topics_id
    def get_tagsId(self, obj):
        return obj.tags_id

# 宣传图
class Banner(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="轮播图编号", help_text="轮播图编号")
    img = models.CharField(max_length=255, verbose_name="图片 ", null=True, blank=True, help_text="图片")
    url = models.CharField(max_length=255, verbose_name="链接地址 ", null=True, blank=True, help_text="链接地址")
    index_radio = models.CharField(max_length=255, verbose_name="是否首页 ", null=True, blank=True, help_text="是否首页")

    @property
    def indexRadio(self):
        return self.index_radio

    class Meta:
        db_table = "banner"
        verbose_name = "宣传图"
        verbose_name_plural = verbose_name

class BannerSerializer(serializers.ModelSerializer):
    indexRadio = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = '__all__'

    def get_indexRadio(self, obj):
        return obj.index_radio

