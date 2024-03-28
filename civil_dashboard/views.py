from django.shortcuts import render

def test_socket(request):
    return render(request, 'test-socket.html',{})


