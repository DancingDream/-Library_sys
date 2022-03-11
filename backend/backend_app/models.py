from django.db import models

# Create your models here.

#书本信息
class Books(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    bookName = models.CharField('书名', max_length=20, null=False)
    subhead = models.CharField('副标题', max_length=20, null=False)
    author = models.CharField('作者', max_length=20, null=False)
    translator = models.CharField('译者', max_length=20, null=True)
    press = models.CharField('出版社', max_length=20, null=False)
    publicationYear = models.IntegerField('出版年份', null=False)
    ISBN = models.IntegerField('ISBN', null=False)
    pagination = models.IntegerField('页数', null=True)
    cover = models.ImageField('封面', null=True)
    prospectus = models.TextField('内容简介', null=True)
    location = models.CharField('收录位置', max_length=20, null=True)
    quantity = models.IntegerField('总数', null=True)
    surplus = models.IntegerField('剩余数', null=True)
    weight = models.IntegerField('权重', null=True)
    class Meta:
        db_table = 'Books'

#用户信息
class Uesr(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    userID = models.CharField('用户账号', db_column='user_ID', max_length=32, null=False)
    passWord = models.CharField('用户密码', db_column='pass_word', max_length=32, null=False)
    nickName = models.CharField('用户昵称', max_length=20, null=False)
    userName = models.CharField('用户姓名', max_length=20, null=False)
    gender = models.CharField('用户性别', max_length=4, null=False)
    age = models.IntegerField('用户年龄', null=False)
    phone = models.CharField('联系电话', max_length=11, null=False)
    address = models.CharField('联系地址', max_length=64, null=False)
    email = models.EmailField('电子邮箱', null=False)
    face = models.ImageField('人脸信息', null=False)
    regDate = models.DateField('注册时间', auto_now=True, null=False)
    weChat = models.CharField('微信号', max_length=32, null=False)
    credit = models.IntegerField('信誉分', null=False)
    book1ID = models.OneToOneField(Books, on_delete=models.PROTECT, related_name='book1ID')
    book2ID = models.OneToOneField(Books, on_delete=models.PROTECT, related_name='book2ID')
    class Meta:
        db_table = 'Uesr'

#管理员信息
class Admin(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    adminID = models.CharField('管理员账号', db_column='adminID', max_length=32, null=False)
    passWord = models.CharField('密码', db_column='pass_word', max_length=32, null=False)
    class Meta:
        db_table = 'Admin'

#记录
class Record(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    borrowerID = models.OneToOneField(Uesr, on_delete=models.PROTECT)
    borrowDate = models.DateField('借书日期', auto_now=True, null=False)
    returnDate = models.DateField('还书时间', null=False)
    deadline = models.IntegerField('期限', null=False)
    class Meta:
        db_table = 'Record'

#数据
class Data(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    countTime = models.DateField('统计时间', auto_now=True, null=False)
    borrowDataNow = models.IntegerField('今日借书人数', null=False)
    returnDataNow = models.IntegerField('今日还书人数', null=False)
    DataNow = models.IntegerField('在借人数', null=False)
    class Meta:
        db_table = 'Data'