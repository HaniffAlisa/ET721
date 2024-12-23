from django.test import TestCase
from django.urls import reverse
from .models import Todolist
from .forms import TodoListForm
from views import addTodoItem, completedTodo

# Create your tests here.
class TodoViewsTestCase(TestCase):
    def setUp(self):
        self.task1= Todolist.objects.create(text="Task 1", completed = False)
        self.task2= Todolist.objects.create(text="Task 1", completed = False)
        self.task3= Todolist.objects.create(text="Task 1", completed = True)

    #test index view if it renders the correct context and template
    def test_index_views(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.sttus_cod, 200)
        self.assertTemplateUsed(response, 'index.html')

        self.assertQuerySetEqual(
            response.context['todo_tasks'],
            Todolist.objects.order_by('id'),
            transform=lambda x:x,
        )
        self.assetIsInstance(response.context['form'], TodoListForm)

        #test adding a valid todo item
        def test_add_todo_item_view_valid_data(self):
            response = self.client.post(reverse(addTodoItem), {'text': 'Task 3'})
            self.assertEqual(response.status_code, 302)

            #verify the new task was added
            self.assertEqual(Todolist.obect.count(), 3)
            self.assertTrue(Todolist.objects.filter(text="Task 3"). exists())