"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from admin import settings
from system.base.dict import *
from system.base.file import *
from system.base.login import *
from system.base.notice import *
from system.base.permission import *
from system.base.register import *
from system.base.role import *
from system.base.user import *
from business.views.student import *
from business.views.teacher import *
from business.views.news import *
from business.views.category import *
from business.views.topics import *
from business.views.prerecord import *
from business.views.records import *
from business.views.pm import *
from business.views.topicstags import *
from business.views.tags import *
from business.views.membertags import *
from business.views.banner import *
from business.views.front import *


urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('logout/<str:id>', LogoutView.as_view()),
    path('user', UserView.as_view(),name="user"),
    path('user/<int:pk>', UserView.as_view(), name='user_detail'),
    path('user/page', UserPageView.as_view(), name="user_page"),
    path('user/del/batch', UserBatchDeleteAPIView.as_view(),name="user_batch_delete"),
    path('user/export', UserExport.as_view(),name="user_export"),
    path('updateUser', UserInfoUpdate.as_view(),name="user_info_update"),
    path('password/change', UserUpdatePwd.as_view(),name="user_update_pwd"),
    path('role', RoleView.as_view(),name="role"),
    path('role/<int:pk>', RoleView.as_view(), name='role_detail'),
    path('role/page', RolePageView.as_view(), name="role_page"),
    path('role/del/batch', RoleBatchDeleteAPIView.as_view(), name="role_batch_delete"),
    path('role/export', RoleExport.as_view(),name="role_export"),
    path('permission', PermissionView.as_view(),name="permission"),
    path('permission/<int:pk>', PermissionView.as_view(), name='permission_delete'),
    path('permission/del/batch', PermissionBatchDeleteAPIView.as_view(), name="permission_batch_delete"),
    path('permission/export', PermissionExport.as_view(),name="permission_export"),
    path('dict', DictView.as_view(), name="dict"),
    path('dict/<int:pk>', DictView.as_view(), name='dict_detail'),
    path('dict/page', DictPageView.as_view(), name="dict_page"),
    path('dict/del/batch', DictBatchDeleteAPIView.as_view(), name="dict_batch_delete"),
    path('dict/export', DictExport.as_view(),name="dict_export"),
    path('file/upload', FileUploadView.as_view(),name="file_upload"),
    path('file/uploadImg', FileUploadEditorView.as_view(),name="file_upload_editor"),
    path('notice', NoticeView.as_view(), name="notice"),
    path('notice/<int:pk>', NoticeView.as_view(), name='notice_detail'),
    path('notice/page', NoticePageView.as_view(), name="notice_page"),
    path('notice/del/batch', NoticeBatchDeleteAPIView.as_view(), name="notice_batch_delete"),
    path('notice/export', NoticeExport.as_view(), name="notice_export"),

    # 用户
    path('student', StudentView.as_view(), name="student"),
    path('student/<int:pk>', StudentView.as_view(), name='student_detail'),
    path('student/page', StudentPageView.as_view(), name="student_page"),
    path('student/del/batch', StudentBatchDeleteAPIView.as_view(), name="student_batch_delete"),
    path('student/export', StudentExport.as_view(), name="student_export"),
    path('front/student/user/<int:userId>', getStudentByUserId.as_view(), name="getStudentByUserId"),
    path('front/student/update', UpdateStudent.as_view(), name="UpdateStudent"),
    # 教师
    path('teacher', TeacherView.as_view(), name="teacher"),
    path('teacher/<int:pk>', TeacherView.as_view(), name='teacher_detail'),
    path('teacher/page', TeacherPageView.as_view(), name="teacher_page"),
    path('teacher/del/batch', TeacherBatchDeleteAPIView.as_view(), name="teacher_batch_delete"),
    path('teacher/export', TeacherExport.as_view(), name="teacher_export"),
    path('front/teacher/user/<int:userId>', getTeacherByUserId.as_view(), name="getTeacherByUserId"),
    path('front/teacher/update', UpdateTeacher.as_view(), name="UpdateTeacher"),

    # 毕设选题指导
    path('news', NewsView.as_view(), name="news"),
    path('news/<int:pk>', NewsView.as_view(), name='news_detail'),
    path('news/page', NewsPageView.as_view(), name="news_page"),
    path('news/del/batch', NewsBatchDeleteAPIView.as_view(), name="news_batch_delete"),
    path('news/export', NewsExport.as_view(), name="news_export"),
    path('front/news/update', UpdateNews.as_view(), name="UpdateNews"),
    # 毕设题目分类
    path('category', CategoryView.as_view(), name="category"),
    path('category/<int:pk>', CategoryView.as_view(), name='category_detail'),
    path('category/page', CategoryPageView.as_view(), name="category_page"),
    path('category/del/batch', CategoryBatchDeleteAPIView.as_view(), name="category_batch_delete"),
    path('category/export', CategoryExport.as_view(), name="category_export"),
    path('front/category/update', UpdateCategory.as_view(), name="UpdateCategory"),
    # 毕设题目
    path('topics', TopicsView.as_view(), name="topics"),
    path('topics/<int:pk>', TopicsView.as_view(), name='topics_detail'),
    path('topics/page', TopicsPageView.as_view(), name="topics_page"),
    path('topics/del/batch', TopicsBatchDeleteAPIView.as_view(), name="topics_batch_delete"),
    path('topics/export', TopicsExport.as_view(), name="topics_export"),
    path('front/topics/update', UpdateTopics.as_view(), name="UpdateTopics"),
    # 待选题记录
    path('prerecord', PrerecordView.as_view(), name="prerecord"),
    path('prerecord/<int:pk>', PrerecordView.as_view(), name='prerecord_detail'),
    path('prerecord/page', PrerecordPageView.as_view(), name="prerecord_page"),
    path('prerecord/del/batch', PrerecordBatchDeleteAPIView.as_view(), name="prerecord_batch_delete"),
    path('prerecord/export', PrerecordExport.as_view(), name="prerecord_export"),
    path('front/prerecord/update', UpdatePrerecord.as_view(), name="UpdatePrerecord"),
    # 毕设选题记录
    path('records', RecordsView.as_view(), name="records"),
    path('records/<int:pk>', RecordsView.as_view(), name='records_detail'),
    path('records/page', RecordsPageView.as_view(), name="records_page"),
    path('records/del/batch', RecordsBatchDeleteAPIView.as_view(), name="records_batch_delete"),
    path('records/export', RecordsExport.as_view(), name="records_export"),
    path('front/records/update', UpdateRecords.as_view(), name="UpdateRecords"),
    # 私聊信息
    path('pm', PmView.as_view(), name="pm"),
    path('pm/<int:pk>', PmView.as_view(), name='pm_detail'),
    path('pm/page', PmPageView.as_view(), name="pm_page"),
    path('pm/del/batch', PmBatchDeleteAPIView.as_view(), name="pm_batch_delete"),
    path('pm/export', PmExport.as_view(), name="pm_export"),
    path('front/pm/update', UpdatePm.as_view(), name="UpdatePm"),
    # 题目标签
    path('tags', TagsView.as_view(), name="tags"),
    path('tags/<int:pk>', TagsView.as_view(), name='tags_detail'),
    path('tags/page', TagsPageView.as_view(), name="tags_page"),
    path('tags/del/batch', TagsBatchDeleteAPIView.as_view(), name="tags_batch_delete"),
    path('tags/export', TagsExport.as_view(), name="tags_export"),
    path('front/tags/update', UpdateTags.as_view(), name="UpdateTags"),
    # 用户标签
    path('membertags', MembertagsView.as_view(), name="membertags"),
    path('membertags/<int:pk>', MembertagsView.as_view(), name='membertags_detail'),
    path('membertags/page', MembertagsPageView.as_view(), name="membertags_page"),
    path('membertags/del/batch', MembertagsBatchDeleteAPIView.as_view(), name="membertags_batch_delete"),
    path('membertags/export', MembertagsExport.as_view(), name="membertags_export"),
    path('front/membertags/update', UpdateMembertags.as_view(), name="UpdateMembertags"),
    # 选题关联标签
    path('topicstags', TopicstagsView.as_view(), name="topicstags"),
    path('topicstags/<int:pk>', TopicstagsView.as_view(), name='topicstags_detail'),
    path('topicstags/page', TopicstagsPageView.as_view(), name="topicstags_page"),
    path('topicstags/del/batch', TopicstagsBatchDeleteAPIView.as_view(), name="topicstags_batch_delete"),
    path('topicstags/export', TopicstagsExport.as_view(), name="topicstags_export"),
    path('front/topicstags/update', UpdateTopicstags.as_view(), name="UpdateTopicstags"),
    #根据选题ID查询标签列表
    path('front/tagsbytopicid/<int:topicsId>', GetTagsByTopicId.as_view(), name="TagsByTopicId"),
    #根据选题ID删除标签列表
    path('front/tagsbytopicid/del/<int:topicsId>', DelTagsByTopicId.as_view(), name="DelTagsByTopicId"),

    # 宣传图
    path('banner', BannerView.as_view(), name="banner"),
    path('banner/<int:pk>', BannerView.as_view(), name='banner_detail'),
    path('banner/page', BannerPageView.as_view(), name="banner_page"),
    path('banner/del/batch', BannerBatchDeleteAPIView.as_view(), name="banner_batch_delete"),
    path('banner/export', BannerExport.as_view(), name="banner_export"),

    # 前台-用户
    path('front/user/list', UserListDetail.as_view(), name="front_user_list"),
    path('front/user/<int:pk>', UserListDetail.as_view(), name='front_user_detail'),
    path('front/user/page', UserPage.as_view(), name="front_user_page"),
    # 前台-网站公告
    path('front/notice/list', NoticeListDetail.as_view(), name="front_notice_list"),
    path('front/notice/<int:pk>', NoticeListDetail.as_view(), name='front_notice_detail'),
    path('front/notice/page', NoticePage.as_view(), name="front_notice_page"),
    # 前台-宣传图
    path('front/banner/list', BannerListDetail.as_view(), name="front_banner_list"),
    path('front/banner', BannerListDetail.as_view(), name="front_banner"),
    path('front/banner/<int:pk>', BannerListDetail.as_view(), name='front_banner_detail'),
    path('front/banner/page', BannerPage.as_view(), name='front_banner_page'),
    # 前台-用户
    path('front/student/list', StudentListDetail.as_view(), name="front_student_list"),
    path('front/student', StudentListDetail.as_view(), name="front_student"),
    path('front/student/<int:pk>', StudentListDetail.as_view(), name='front_student_detail'),
    path('front/student/page', StudentPage.as_view(), name='front_student_page'),
    # 前台-教师
    path('front/teacher/list', TeacherListDetail.as_view(), name="front_teacher_list"),
    path('front/teacher', TeacherListDetail.as_view(), name="front_teacher"),
    path('front/teacher/<int:pk>', TeacherListDetail.as_view(), name='front_teacher_detail'),
    path('front/teacher/page', TeacherPage.as_view(), name='front_teacher_page'),
    # 前台-毕设选题指导
    path('front/news/list', NewsListDetail.as_view(), name="front_news_list"),
    path('front/news', NewsListDetail.as_view(), name="front_news"),
    path('front/news/<int:pk>', NewsListDetail.as_view(), name='front_news_detail'),
    path('front/news/page', NewsPage.as_view(), name='front_news_page'),
    # 前台-毕设题目分类
    path('front/category/list', CategoryListDetail.as_view(), name="front_category_list"),
    path('front/category', CategoryListDetail.as_view(), name="front_category"),
    path('front/category/<int:pk>', CategoryListDetail.as_view(), name='front_category_detail'),
    path('front/category/page', CategoryPage.as_view(), name='front_category_page'),
    # 前台-毕业选题列表
    path('front/topics/list', TopicsListDetail.as_view(), name="front_topics_list"),
    path('front/topics', TopicsListDetail.as_view(), name="front_topics"),
    path('front/topics/<int:pk>', TopicsListDetail.as_view(), name='front_topics_detail'),
    path('front/topics/page', TopicsPage.as_view(), name='front_topics_page'),
    # 前台-待选题记录
    path('front/prerecord/list', PrerecordListDetail.as_view(), name="front_prerecord_list"),
    path('front/prerecord', PrerecordListDetail.as_view(), name="front_prerecord"),
    path('front/prerecord/<int:pk>', PrerecordListDetail.as_view(), name='front_prerecord_detail'),
    path('front/prerecord/page', PrerecordPage.as_view(), name='front_prerecord_page'),
    # 前台-毕设选题记录
    path('front/records/list', RecordsListDetail.as_view(), name="front_records_list"),
    path('front/records', RecordsListDetail.as_view(), name="front_records"),
    path('front/records/<int:pk>', RecordsListDetail.as_view(), name='front_records_detail'),
    path('front/records/page', RecordsPage.as_view(), name='front_records_page'),
    # 前台-私聊信息
    path('front/pm/list', PmListDetail.as_view(), name="front_pm_list"),
    path('front/pm', PmListDetail.as_view(), name="front_pm"),
    path('front/pm/<int:pk>', PmListDetail.as_view(), name='front_pm_detail'),
    path('front/pm/page', PmPage.as_view(), name='front_pm_page'),
    # 前台-题目标签
    path('front/tags/list', TagsListDetail.as_view(), name="front_tags_list"),
    path('front/tags', TagsListDetail.as_view(), name="front_tags"),
    path('front/tags/<int:pk>', TagsListDetail.as_view(), name='front_tags_detail'),
    path('front/tags/page', TagsPage.as_view(), name='front_tags_page'),
    # 前台-我的选题标签
    path('front/membertags/list', MembertagsListDetail.as_view(), name="front_membertags_list"),
    path('front/membertags', MembertagsListDetail.as_view(), name="front_membertags"),
    path('front/membertags/<int:pk>', MembertagsListDetail.as_view(), name='front_membertags_detail'),
    path('front/membertags/page', MembertagsPage.as_view(), name='front_membertags_page'),
    # 前台-选题关联标签
    path('front/topicstags/list', TopicstagsListDetail.as_view(), name="front_topicstags_list"),
    path('front/topicstags', TopicstagsListDetail.as_view(), name="front_topicstags"),
    path('front/topicstags/<int:pk>', TopicstagsListDetail.as_view(), name='front_topicstags_detail'),
    path('front/topicstags/page', TopicstagsPage.as_view(), name='front_topicstags_page'),

    #修改购物车
    path('front/prerecord/update', UpdatePrerecord.as_view(), name="front_updatePrerecord"),


    #添加/修改订单
    path('front/records/update', UpdateRecords.as_view(), name="front_updateRecords"),
    #取消订单
    path('front/records/cancel/<int:pk>', CancelRecords.as_view(), name="front_cancelRecords"),


    #统计-毕设选题分类数量
    path('statistics/categoryCount', categoryCountView.as_view(), name="statistics_categoryCount"),
    #统计-毕设题目数量
    path('statistics/topicsCount', topicsCountView.as_view(), name="statistics_topicsCount"),
    #统计-学生数量
    path('statistics/studentCount', studentCountView.as_view(), name="statistics_studentCount"),
    #统计-选题记录数量
    path('statistics/recordsCount', recordsCountView.as_view(), name="statistics_recordsCount"),
    #统计-选题分类数量统计
    path('statistics/topicsCategory', topicsCategoryView.as_view(), name="statistics_topicsCategory"),
    #统计-毕设题目选题人数统计
    path('statistics/recordsStatics', recordsStaticsView.as_view(), name="statistics_recordsStatics"),



    # 添加推荐标签
    path('front/membertags/<int:tagsId>/<int:userId>', AddTags.as_view(), name="front_addtags"),
    # 删除推荐标签
    path('front/membertags/del/<int:tagsId>/<int:userId>', DeleteTags.as_view(), name="front_deletetags"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
