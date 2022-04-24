from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from . import models
from django.template import loader
from django.http import Http404
from django.urls import reverse
from .models import Choice, Question
import os
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
import requests


# Create your views here.


def index(requests):
    #return render(requests, 'podlist.html')
    ##return render(requests, 'index.html')
    #return HttpResponse("welcome my website")
    latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(requests, 'index.html', context)


def home(req):
    print("request content is %s" % req)
    print(type(req))

    pod = req.POST.get('pod')
    pod_name = pod.replace("\r\n", "\n")
    print("podname is %s " % pod_name, "podname type is", type(pod_name))
    # poddelete = os.system("kubectl describe pod %s" % podname)
    # poddelete = os.popen("kubectl delete pod %s"%(pod_name))
    result = {"status": 0, "msg": "", "pod_name": pod_name}
    result1 = os.popen("kubectl delete pod %s" % (pod_name))
    # logger.error(result1.readlines())
    return HttpResponse(json.dumps(result, bigint_as_string=True), content_type='application/json')
    # print("delete pod is", poddelete)
    # return HttpResponse("pod delete success %s" % poddelete)

# def kill_pod(request):
#     pod_name = request.POST.get('pod_name')
#     logger.error(pod_name)
#     result = {"status":0,"msg":"","pod_name":pod_name}
#     result1 = os.popen("kubectl delete pod %s"%(pod_name))
#     logger.error(result1.readlines())
#     return HttpResponse(json.dumps(result, cls=ExtendJSONEncoder, bigint_as_string=True),
#                         content_type='application/json')


def detail(request, question_id):
    return HttpResponse("you are looking at question %s." % question_id)
    # try:
    #     question = models.Question.objects.get(pk=question_id)
    # except models.Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'detail.html', {'question': question})
    # question = get_object_or_404(models.Question, pk=question_id)
    # return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    # pass
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


def test(requests):
    #return render(requests, 'test.html', locals())
    dict = {"username": "zhiliao", "age": 18}
    #result = json.dumps(dict)
    # 指定返回数据类型为json且编码为utf-8
    #return HttpResponse(result, content_type='application/json;charset=utf-8')
    return JsonResponse(dict)
    #persons = ['张三', '李四', '王五']
    #return HttpResponse(persons)


def send_message(message):
    #告警测试
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/4ab2e300-90cf-44d7-a41e-566fe8f2b14d"
    payload_message = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))
    return response


@csrf_exempt
def webhook(requests):
    if requests.method == 'POST':
        content = requests.POST
        postBody = requests.body
        print("content type is", type(content))
        print("postBody type is", type(postBody))
        print("content is", content)
        print("postBody is", postBody)
        json_result = json.loads(postBody)
        print("json_result is ", json_result)
        print("json_result type is ", type(json_result))
        print("alert message is", json_result['message'])
        alertmessage = json_result['message']
        allalert = json_result['evalMatches']
        for i in range(len(allalert)):
            example = allalert[i]['metric']
            alertmsg = "告警信息: {0}, 实例对象: {1}".format(alertmessage, example)
            send_message(alertmsg)

        #nodeip = json_result['evalMatches'][0]['metric']
        #print("nodeip type is", type(nodeip))
        #print("nodeip is", nodeip)
        #alertmsg = "告警信息: {0}, 实例对象: {1}".format(alertmessage, nodeip)
        #send_message(alertmsg)
        #print("metric is ", json_result['evalMatches'][1]['metric'])
        #print("nodeip is", json_result[1][''])
        return HttpResponse("print done")
    else:
        return HttpResponse("get metheod is not post")
        print("not post")
