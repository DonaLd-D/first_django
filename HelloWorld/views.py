from django.shortcuts import render


def demo01(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'demo01.html', context)


def demo02(request):
    views_name = "菜鸟教程"
    return render(request, "demo02.html", {"name": views_name})


def demo03(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "demo03.html", {"views_list": views_list})


def demo04(request):
    views_dict = {"name": "菜鸟教程"}
    return render(request, "demo04.html", {"views_dict": views_dict})


def demo05(request):
    name = 0
    return render(request, "demo05.html", {"name": name})


def demo06(request):
    name = "菜鸟教程"
    return render(request, "demo06.html", {"name": name})


def demo07(request):
    num = 1024
    return render(request, "demo07.html", {"num": num})


def demo08(request):
    import datetime
    now = datetime.datetime.now()
    return render(request, "demo08.html", {"time": now})


def demo09(request):
    views_str = "菜鸟教程"
    return render(request, "demo09.html", {"views_str": views_str})


def demo10(request):
    views_str = "<a href='https://www.runoob.com/' target='_blank'> 点击跳转</a>"
    return render(request, "demo10.html", {"views_str": views_str})


def demo11(request):
    views_num = 88
    return render(request, "demo11.html", {"num": views_num})


def demo12(request):
    views_list = ["菜鸟教程", "菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "demo12.html", {"views_list": views_list})


def demo13(request):
    views_dict = {"name": "菜鸟教程", "age": 18}
    return render(request, "demo13.html", {"views_dict": views_dict})


def demo14(request):
    views_list = ["a", "b", "c", "d", "e"]
    return render(request, "demo14.html", {"listvar": views_list})


def demo15(request):
    views_list = []
    return render(request, "demo15.html", {"listvar": views_list})
