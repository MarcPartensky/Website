from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

from home.context import hydrate, base

from django.contrib.auth.forms import AuthenticationForm

# @hydrate(base)
# def login_view(request, context={}):
#     """Custom login view"""
#     if request.method=='POST':
#         form = AuthenticationForm(data = request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username = request.POST['username'],
#                 password = request.POST['password'],
#             )
#             if user is not None:
#                 messages.add_message(request, messages.SUCCESS,
#                                      "Welcome back, {}".format(user))
#                 login(request, user,
#                       backend = 'django.contrib.auth.backends.ModelBackend')
#                 print('user authenticated:', user.is_authenticated)
#                 print('user active:', user.is_active)
#                 return redirect('profile')

#         messages.add_message(request, messages.ERROR,
#             f"Invalid user.")
#         print('Invalid user')
#         context['form'] = AuthenticationForm()
#         return render(request, 'users/login.html', context)

#     elif request.method == 'GET':
#         context['form'] = AuthenticationForm()
#         return render(request, 'users/login.html', context)

#     else:
#         raise Exception(f"{request.method} is an unsupported method type.\n\
#                         Use GET or POST methods instead.")

class LoginView(auth_views.LoginView):
    """Login view hydrated with context."""
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context

    @classmethod
    def as_view(cls, *args, **kwargs):
        """Force authentication."""
        f = super().as_view(*args, **kwargs)
        @csrf_protect
        def view(request):
            if request.method == 'POST':
                # form = AuthenticationForm(data = request.POST)
                # if form.is_valid():
                user = authenticate(
                    username = request.POST['username'],
                    password = request.POST['password']
                )
                login(request, user)
                print('user authenticated:', user.is_authenticated)
                for key, value in request.session.items():
                    print('{} => {}'.format(key, value))
                return redirect('profile')
            return f(request)
        return view


class PasswordResetView(auth_views.PasswordResetView):
    """Password reset view hydrated with context."""
    template_name = 'users/password_reset.html'
    # authentication_form = AuthenticationForm

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context


class LogoutView(auth_views.LogoutView):
    """Logout view hydrated with context."""
    template_name = 'users/logout.html'

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """Password reset done view hydrated with context."""
    template_name='users/password_reset_done.html'

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """Password reset confirm view hydrated with context."""
    template_name='users/password_reset_confirm.html'

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    """Password reset complete view hydrated with context."""
    template_name='users/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        """Compute the context."""
        context = super().get_context_data(**kwargs)
        context.update(base(self.request))
        return context


@hydrate(base)
def register(request, context={}):
    """Register view that sends web forms and receives them."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                f'Your account has been created! You are now able to log in as {username}.')
            return redirect('login')
    elif request.method == 'GET':
        form = UserRegisterForm()
    else:
        raise Exception(f'HTTP {request.method} method is not supported.')
    context['form'] = form
    return render(request, 'users/register.html', context)

@login_required
@hydrate(base)
def profile(request, context={}):
    """Show profile view."""
    # print all session variables
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))

    print('user authenticated:', request.user.is_authenticated)
    print('user active:', request.user.is_active)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,
                f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context.update({
        'u_form' : u_form,
        'p_form' : p_form
    })
    return render(request, 'users/profile.html', context)

@login_required
@hydrate(base)
def public_profile(request, context={}):
    """Show profile view."""
    # print all session variables
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))

    print('user authenticated:', request.user.is_authenticated)
    print('user active:', request.user.is_active)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,
                f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context.update({
        'u_form' : u_form,
        'p_form' : p_form
    })
    return render(request, 'users/profile.html', context)
