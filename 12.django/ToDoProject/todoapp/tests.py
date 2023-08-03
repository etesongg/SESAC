from django.test import TestCase
from django.urls import reverse
from .models import ToDo

# Create your tests here.
class TestModelTests(TestCase): 
    def test_str_representation(self):
        task = ToDo.objects.create(title='Test Task', description='테스트')
        self.assertEqual(str(task),'Test Task') # 만약 모델에서 f'타이들: {self.title}' 이라면 '타이틀: Test Task'라고 적어주면 됨(결과가 같게 나와야 하기 때문)

    def test_str_representation2(self):
        task = ToDo.objects.create(title='아무글자', description='테스트')
        self.assertEqual(str(task),'아무글자')

class TaskViewTests(TestCase):
    def test_task_list_view(self):
        response = self.client.get(reverse('todo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo.html')
        # print(response)
        # print(response.status_code)
        # print(response.content)

    def test_task_detail_view(self):
        task = ToDo.objects.create(title='Test1', description='Test11')
        response = self.client.get(reverse('todo_view', args=(task.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_view.html')
        self.assertContains(response, 'Test1')
        self.assertContains(response, 'Test11')

    def test_task_create_view(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/create.html')

        data = {
            'title': 'Test2',
            'description': 'This is my test case 2'
        }
        data2 = {
            'title': 'Test2',
            'description': 'This is my test case 2'
        }

        response = self.client.post(reverse('create'), data)
        self.assertEqual(response.status_code, 302) # 우리가 redirect 했기 때문에
        self.assertEqual(ToDo.objects.count(), 1)

        response = self.client.post(reverse('create'), data2)
        self.assertEqual(ToDo.objects.count(), 2)

    def test_task_update_view(self):
        task = ToDo.objects.create(title='Test Task', description = 'Update Test')
        response = self.client.get(reverse('update', args=(task.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/update.html')

        # 컨텐츠 확인
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Update Test')
        # 업데이트 수행
        update_data = {
            'new_title': 'Update Task',
            'new_description': 'Update Test Again'
        }

        response = self.client.post(reverse('update', args=(task.pk,)), update_data)

        # 전달될 데이터가 잘 반영 되는지 확인
        print(response.status_code)
        self.assertEqual(response.status_code, 302)

        # db로부터 task 내용을 재갱신
        task.refresh_from_db()
        self.assertEqual(task.title, 'Update Task')


    def test_task_delete_view(self):
        task = ToDo.objects.create(title='Test Task', description = 'Delete Test')
        self.assertEqual(ToDo.objects.count(), 1)

        # 지우는 코드
        response = self.client.post(reverse('delete',args=(task.pk,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToDo.objects.count(), 0)

  





        