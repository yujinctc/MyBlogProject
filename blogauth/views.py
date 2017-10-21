

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from blogauth.models import User
from .forms import RegisterForm


from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html')


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    login_form = AuthenticationForm()
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        register_form = RegisterForm(request.POST)


        # 验证数据的合法性
        if register_form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            register_form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        register_form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'blogauth/register.html', context={'register_form': register_form,'form':login_form, 'next': redirect_to})


class BlogLoginView(LoginView):

    # login_form = AuthenticationForm ()
    register_form = RegisterForm ()
    extra_context = {'register_form': register_form}


class RegisterView(TemplateView):

    form_class = RegisterForm

    template_name = 'blogauth/register.html'



    login_form = AuthenticationForm ()

    def get(self, request, *args, **kwargs):
        redirect_to = request.GET.get ('next', request.GET.get ('next', ''))
        register_form = self.form_class()
        return render(request, self.template_name, context={'register_form': register_form,'login_form':self.login_form, 'next': redirect_to})

    def post(self, request, *args, **kwargs):
        redirect_to = request.POST.get ('next', request.GET.get ('next', ''))

        register_form = self.form_class(request.POST)
        # 验证数据的合法性
        if register_form.is_valid ():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            register_form.save ()

            if redirect_to:
                return redirect (redirect_to)
            else:
                return redirect ('/')

        return render(request, self.template_name, context={'register_form': register_form,'login_form':self.login_form, 'next': redirect_to})


