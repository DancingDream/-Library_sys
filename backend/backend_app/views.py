import datetime
import json
import uuid

from backend_app.function import other

import requests
from django.core.cache import cache
from django.http import HttpResponse
from django.views import View

from backend_app import models

# Create your views here.


'''
基础处理类，其他处理继承这个类
'''
class BaseView(View):
    '''
    检查指定的参数是否存在
    存在返回 True
    不存在返回 False
    '''
    def isExit(param):

        if (param == None) or (param == ''):
            return False
        else:
            return True

    '''
    转换分页查询信息
    '''
    def parasePage(pageIndex, pageSize, pageTotal, count, data):

        return {'pageIndex': pageIndex, 'pageSize': pageSize, 'pageTotal': pageTotal, 'count': count, 'data': data}

    '''
    成功响应信息
    '''
    def success(msg='处理成功'):
        resl = {'code': 0, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    '''
    成功响应信息, 携带数据
    '''
    def successData(data, msg='处理成功'):
        resl = {'code': 0, 'msg': msg, 'data': data}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    '''
    系统警告信息
    '''
    def warn(msg='操作异常，请重试'):
        resl = {'code': 1, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    '''
    系统异常信息
    '''
    def error(msg='系统异常'):
        resl = {'code': 2, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')


'''
管理员
'''
class AdminView(BaseView):

    def get(self, request, module, *args, **kwargs):
        if module == 'exit':
            return AdminView.exit(request)
        elif module == 'info':
            return AdminView.getessionInfo(request)
        elif module == 'data':
            return AdminView.getRecordData(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):
        if module == 'login':
            return AdminView.login(request)
        elif module == 'info':
            return AdminView.updSessionInfo(request)
        elif module == 'pwd':
            return AdminView.updSessionPwd(request)
        elif module == 'register':
            return AdminView.register(request)
        else:
            return BaseView.error()

    '''
    用户登陆处理
    '''
    def login(request):

        ID = request.POST.get('adminID')
        passWord = request.POST.get('passWord')

        print(ID)
        print(passWord)

        admin = models.Admins.objects.filter(adminID=ID)

        # print(admin.exists())
        if (admin.exists()):
            admin = admin.first()
            if admin.passWord == passWord:
                token = uuid.uuid4()

                login_user = {
                    'adminID' : admin.adminID,
                    'passWord': admin.passWord,
                    'name': admin.name,
                    'jobNum': admin.jobNum,
                    'phone': admin.phone,
                    'addTime': str(admin.addTime),
                }

                resl = {
                    'token': str(token)
                }

                cache.set(token, login_user, 60 * 60 * 60 * 3)

                return AdminView.successData(resl)

        else:
            return AdminView.error('用户名或密码输入错误')

    '''
    用户登出处理
    '''
    def exit(request):

        token = request.GET.get('token')

        cache.delete(token)

        return BaseView.success()

    '''
    用户注册处理
    '''
    def register(request):
        adminID = request.POST.get('adminID')
        jobNum = request.POST.get('jobNum')

        if(models.Admins.objects.filter(adminID=adminID) or models.Admins.objects.filter(jobNum=jobNum)):
            return AdminView.error('用户已存在，请重新注册')
        else:
            models.Admins.objects.create(
                adminID = request.POST.get('adminID'),
                passWord=request.POST.get('repassWord'),
                name=request.POST.get('name'),
                jobNum=request.POST.get('jobNum'),
                phone=request.POST.get('phone'),
            )
            return BaseView.success()

    '''
    获取登录用户信息处理
    '''
    def getessionInfo(request):
        token = request.GET.get('token')
        return BaseView.successData(cache.get(token))

    '''
    修改登陆用户信息
    '''
    def updSessionInfo(request):

        token = request.POST.get('token')
        loginUser = cache.get(token)

        print(loginUser)

        if(models.Admins.objects.filter(userID=loginUser['userID'])):
            return AdminView.error('用户账号已存在，请重新填写')
        else:
            models.Admins.objects.filter(jobNum=loginUser['jobNum']).update(
                userID=request.POST.get('userID'),
                phone=request.POST.get('phone'),
            )

            return BaseView.success()

    '''
    修改登陆用户密码
    '''
    def updSessionPwd(request):

        token = request.POST.get('token')
        loginUser = cache.get(token)

        models.Admins.objects.filter(jobNum=loginUser['jobNum']).update(
            passWord=request.POST.get('newPwd'),
        )

        return BaseView.success()

    '''
    用户端首页获取数据
    '''
    def getRecordData(request):
        bookNum = models.Books.objects.filter(state=True)

        today = datetime.date.today()

        bookNum = bookNum.count()

        boNum = models.Notices.objects.filter(addTime=today)
        boNum = boNum.count()
        reNum = models.Notices.objects.filter(amenTime=today)
        reNum = reNum.count()

        data ={
            'bookNum': bookNum,
            'reNum': reNum,
            'boNum': boNum,
        }

        return BaseView.successData(data)


'''
书本
'''
class BooksView((BaseView)):

    def get(self, request, module, *args, **kwargs):
        if module == 'info':
            return BooksView.getBooksInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):
        if module == 'add':
            return BooksView.addBook(request)
        elif module == 'new':
            return BooksView.fineNewBook(request)
        elif module == 'amend':
            return BooksView.amendBook(request)
        else:
            return BaseView.error()

    # 获取书本信息
    def getBooksInfo(request):
        resl = []
        data = models.Books.objects.all().order_by('weight')
        for item in data:
            temp = {
                'bookName': item.bookName,
                'subhead': item.subhead,
                'originalName': item.originalName,
                'author': item.author,
                'translator': item.translator,
                'ISBN': item.ISBN,
                'cover': str(item.cover),
                'price': item.price,
                'chinaClass': item.chinaClass,
                'page': item.page,
                'category': item.category,
                'pubDate': item.pubDate,
                'pubLisher': item.pubLisher,
                'pubLisherAdd': item.pubLisherAdd,
                'binding': item.binding,
                'language': item.language,
                'prospectus': item.prospectus,
                'location': item.location,
                'quantity': item.quantity,
                'surplus': item.surplus,
                'weight': item.weight,
                'state': item.state
            }
            resl.append(temp)
        return BaseView.successData(resl)

    # 利用isbn查找书
    def fineNewBook(request):
        newISBN = request.POST.get('isbn')
        book = models.Books.objects.filter(ISBN=newISBN)
        resl = []
        # return BaseView.success()
        #
        if (book.exists()):

            data = book.first()
            temp = {
                'bookName': data.bookName,
                'subhead': data.subhead,
                'originalName': data.originalName,
                'author': data.author,
                'translator': data.translator,
                'ISBN': data.ISBN,
                'cover': data.cover,
                'price': data.price,
                'chinaClass': data.chinaClass,
                'page': data.page,
                'category': data.category,
                'pubDate': data.pubDate,
                'pubLisher': data.pubLisher,
                'pubLisherAdd': data.pubLisherAdd,
                'binding': data.binding,
                'language': data.language,
                'prospectus': data.prospectus,
                'location': data.location,
                'quantity': data.quantity,
                'surplus': data.surplus,
                'weight': data.weight,
                'state': data.state,
            }
            resl.append(temp)

        else:
            key = '5932e79c50a64776805ff70883647676'
            url = 'https://api.ibook.tech/v1/book/isbn?isbn=' + newISBN + '&uKey=' +key
            resp = requests.get(url)
            data = resp.json()

            if(data['errcode'] == 2008):
                return BaseView.error('请输入正确的ISBN')

            else:
                resp = (data['data'])

                if 'translator' in resp:
                    translator = resp['translator']
                else :
                    translator = None

                if 'page' in resp:
                    page = resp['page']
                else :
                    page = None

                models.Books.objects.create(
                    bookName = resp['title'],
                    author = resp['author'],
                    translator = translator,
                    ISBN = resp['isbn'],
                    cover = resp['img'],
                    price = resp['price'],
                    chinaClass=resp['chinaclass'],
                    page=page,
                    category=resp['category'],
                    pubDate=resp['pubdate'],
                    pubLisher=resp['publisher'],
                    pubLisherAdd=resp['publisherAddress'],
                    binding=resp['binding'],
                    language=resp['language'],
                    prospectus=resp['summary'],
                    state=False,
                )
                temp = {
                    'bookName': resp['title'],
                    'author': resp['author'],
                    'translator': translator,
                    'ISBN': resp['isbn'],
                    'cover': resp['img'],
                    'price': resp['price'],
                    'chinaClass': resp['chinaclass'],
                    'page': page,
                    'category': resp['category'],
                    'pubDate': resp['pubdate'],
                    'pubLisher': resp['publisher'],
                    'pubLisherAdd': resp['publisherAddress'],
                    'binding': resp['binding'],
                    'language': resp['language'],
                    'prospectus': resp['summary'],
                    'state' : False,
                }
                resl.append(temp)

        return BaseView.successData(resl)

    # 添加新书
    def addBook(request):

        ISBN = request.POST.get('ISBN')

        if (request.POST.get('state') == 'false'):
            state = False
        else:
            state = True
        # weight = book.get('weight')

        models.Books.objects.update_or_create(ISBN=ISBN,defaults=
        {
            'bookName': request.POST.get('bookName'),
            'author': request.POST.get('author'),
            'translator': request.POST.get('translator'),

            'cover': request.POST.get('cover'),
            'price': request.POST.get('price'),
            'chinaClass': request.POST.get('chinaClass'),
            'page': request.POST.get('page'),
            'category': request.POST.get('category'),
            'pubDate': request.POST.get('pubDate'),
            'pubLisher': request.POST.get('pubLisher'),
            'pubLisherAdd': request.POST.get('pubLisherAddress'),
            'binding': request.POST.get('binding'),
            'language': request.POST.get('language'),
            'prospectus': request.POST.get('prospectus'),
            'location': request.POST.get('location'),
            'quantity': request.POST.get('quantity'),
            'surplus': request.POST.get('quantity'),
            'weight': request.POST.get('weight'),
            'state': state,
        })
        return BooksView.success()

    # 修改书本信息
    def amendBook(request):
        ISBN = request.POST.get('isbn')
        book = models.Books.objects.filter(ISBN=ISBN)
        record = models.Record.objects.filter(
            borrowerBook=book.first(),
            state=True,
        )

        if (book.exists()):
            book = book.first()

            surplus = book.quantity - record.count()

            book.update(
                bookName=request.POST.get('title'),
                author=request.POST.get('author'),
                translator=request.POST.get('translator'),
                ISBN=request.POST.get('isbn'),
                cover=request.POST.get('img'),
                price=request.POST.get('price'),
                chinaClass=request.POST.get('chinaclass'),
                page=request.POST.get('page'),
                category=request.POST.get('category'),
                pubDate=request.POST.get('pubdate'),
                pubLisher=request.POST.get('publisher'),
                pubLisherAdd=request.POST.get('publisherAddress'),
                binding=request.POST.get('binding'),
                language=request.POST.get('language'),
                prospectus=request.POST.get('prospectus'),
                location=request.POST.get('location'),
                quantity=request.POST.get('quantity'),
                surplus=surplus,
                weight=request.POST.get('weight'),
                state=request.POST.get('state'),
            )
            return BaseView.success()


'''
公告
'''
class NoticeView((BaseView)):
    def get(self, request, module, *args, **kwargs):
        if module == 'getInfo':
            return NoticeView.getNoticeInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):
        if module == 'add':
            return NoticeView.newNotice(request)
        elif module == 'amen':
            return NoticeView.amenNotice(request)
        else:
            return BaseView.error()

    def getNoticeInfo(request):
        resl = []
        data = models.Notices.objects.all().order_by('-amenTime')
        for item in data:
            temp = {
                'title': item.title,
                'text': item.text,
                'addTime': str(item.addTime),
                'amenTime': str(item.amenTime),
                'setEdit': item.setEdit.name,
            }
            resl.append(temp)
        return BaseView.successData(resl)

    def newNotice(request):
        token = request.POST.get('token')
        loginUser = cache.get(token)
        print(loginUser)
        print(token)

        models.Notices.objects.create(
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            setEdit=models.Admins.objects.filter(jobNum=loginUser['jobNum']).first(),
        )

        return BaseView.success()

    def amenNotice(request):

        addTime = request.POST.get('addTime')

        token = request.POST.get('token')
        loginUser = cache.get(token)

        models.Notices.objects.filter(addTime=addTime).update(
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            setEdit=models.Admins.objects.filter(jobNum=loginUser['jobNum']).first(),
        )

        return BaseView.success()

'''
用户
'''
class UserView((BaseView)):
    def get(self, request, module, *args, **kwargs):
        if module == 'info':
            return UserView.getessionInfo(request)
        elif module == 'exit':
            return UserView.exit(request)
        elif module == 'infos':
            return UserView.getUsersInfo(request)
        elif module == 'record':
            return UserView.getUsersRecord(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):
        if module == 'register':
            return UserView.register(request)
        elif module == 'login':
            return UserView.login(request)
        elif module == 'upState':
            return UserView.updateUserState(request)
        else:
            return BaseView.error()

    def register(request):

        userID = request.POST.get('userID')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        print(request.POST.get('userID'))
        print(request.POST.get('phone'))

        if (models.Uesr.objects.filter(userID=userID) or models.Uesr.objects.filter(phone=phone) or models.Uesr.objects.filter(email=email)):
            return UserView.error('用户已存在，请重新注册')
        else:
            models.Uesr.objects.create(
                userID=request.POST.get('userID'),
                passWord=request.POST.get('repassWord'),
                userName=request.POST.get('userName'),
                nickName=request.POST.get('nickName'),

                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                borrowingBook=0,
                banState=False,
            )
            return BaseView.success()


    def login(request):

        ID = request.POST.get('userID')
        passWord = request.POST.get('passWord')

        userID = models.Uesr.objects.filter(userID=ID)
        phone = models.Uesr.objects.filter(phone=ID)
        email = models.Uesr.objects.filter(email=ID)


        # print(admin.exists())
        if(userID.exists() or phone.exists() or email.exists()):
            if (userID.exists()):
                userID = userID.first()
            elif(phone.exists()):
                userID = phone.first()
            else:
                userID = email.first()

            if userID.passWord == passWord:
                token = uuid.uuid4()

                login_user = {
                    'userID': userID.userID,
                    'passWord': userID.passWord,
                    'nickName': userID.nickName,
                    'userName': userID.userName,
                    'email': userID.email,
                    'regDate': str(userID.regDate),
                    'borrowingBook': userID.borrowingBook,
                    'banState': userID.banState
               }

                resl = {
                    'token': str(token)
                }

                cache.set(token, login_user, 60 * 60 * 60 * 3)

                print(cache.get(token))

                return UserView.successData(resl)

            else:
                return UserView.error('用户名或密码输入错误')

        else:
            return UserView.error('用户名或密码输入错误')


    '''
    获取登录用户信息处理
    '''
    def getessionInfo(request):
        token = request.GET.get('token')
        return BaseView.successData(cache.get(token))

    '''
    用户登出处理
    '''
    def exit(request):

        token = request.GET.get('token')

        cache.delete(token)

        return BaseView.success()

    '''
    获取用户信息
    '''
    def getUsersInfo(request):
        resl = []
        data = models.Uesr.objects.all().order_by('-regDate')
        for item in data:
            temp = {
                'userID': item.userID,
                'nickName': item.nickName,
                'userName': item.userName,
                'phone': item.phone,
                'email': item.email,
                'regDate': str(item.regDate),
                'borrowingBook': item.borrowingBook,
                'banState': item.banState,
            }
            resl.append(temp)
        return BaseView.successData(resl)

    '''
    更新用户状态
    '''
    def updateUserState(request):
        userID = request.POST.get('userID')
        banState = request.POST.get('banState')

        user = models.Uesr.objects.filter(userID=userID).first()
        print(user.banState)

        user.banState = bool(1-user.banState)
        user.save()

        return BaseView.success()


'''
记录类
'''
class RecordView((BaseView)):
    def get(self, request, module, *args, **kwargs):
        if module == 'infos':
            return RecordView.getRecordInfo(request)
        else:
            return BaseView.error()

    def post(self, request, module, *args, **kwargs):
        if module == 'reBook':
            return RecordView.reBook(request)
        elif module == 'boBook':
            return RecordView.boBook(request)
        else:
            return BaseView.error()

    '''
    借书
    '''
    def boBook(request):

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        isbn = request.POST.get('isbn')

        record = models.Record.objects.filter(
            borrowerID=models.Uesr.objects.filter(userName=name, phone=phone).first(),
            borrowerBook=models.Books.objects.filter(ISBN=isbn).first(),
            state=True,
        )
        user = models.Uesr.objects.filter(userName=name, phone=phone)
        book = models.Books.objects.filter(ISBN=isbn)

        if(user.exists()):
            user = user.first()
            if(book.exists()):
                book = book.first()

                if(book.surplus == 0):
                    return RecordView.error('该书无库存')

                elif(user.banState == True):
                    return RecordView.error('用户已禁用，请联系管理员')

                elif(user.borrowingBook <= 2 ):
                    # state报错，需要循环便利state列状态
                    if(record.exists()):
                         return RecordView.error('该书已借用')

                    else:
                        book.surplus = book.surplus -1
                        book.save()
                        models.Record.objects.create(
                            borrowerID=user,
                            borrowerBook=book,
                            deadline=30,
                            state=True,
                        )

                        return BaseView.success()

                else:
                    return RecordView.error('借书超过上限')
            else:
                return RecordView.error('书本不存在')
        else:
            return RecordView.error('个人信息错误，请重新填写')

    '''
    还书
    '''
    def reBook(request):

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        isbn = request.POST.get('isbn')

        record = models.Record.objects.filter(
            borrowerID=models.Uesr.objects.filter(userName=name, phone=phone).first(),
            borrowerBook=models.Books.objects.filter(ISBN=isbn).first(),
            state=True,
        )
        user = models.Uesr.objects.filter(userName=name, phone=phone)
        book = models.Books.objects.filter(ISBN=isbn)

        if (user.exists()):
            # user = user.first();
            if (book.exists()):
                book = book.first()

                if (record.exists()):
                    record.update(
                        # returnDate=datetime.date.today(),
                        state=False,
                    )
                    book.surplus = book.surplus + 1
                    book.save()


                    return RecordView.success('成功还书')

                else:
                    return RecordView.error('该书未借用')

            else:
                return RecordView.error('书本不存在')

        else:
            return RecordView.error('个人信息错误，请重新填写')

    '''
    获取记录信息
    '''
    def getRecordInfo(request):

        data = models.Record.objects.all().order_by('-borrowDate', '-id')
        resl = other.bookStateFunction(data)
        return BaseView.successData(resl)

    def getUsersRecord(request):
        token = request.GET.get('token')
        user = cache.get(token)


        data = models.Record.objects.filter(
            borrowerID=models.Uesr.objects.filter(userID=user.userID)
        ).order_by('-borrowDate', '-id')
        resl = RecordView.bookStateFunction(data)

        return BaseView.successData(resl)

