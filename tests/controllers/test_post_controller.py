from test_base import BaseTestCase
from factories import PostFactory
from app.models import Post


class PostApiTests(BaseTestCase):

    def setUp(self):
        PostFactory.create_batch(10)

    def tearDown(self):
        Post.query.delete()

    def test_should_return_10_posts(self):
        response = self.client.get("/posts/")
        print response.json
        self.assertEqual(len(response.json['posts']), 10)

    def test_each_post_in_json_should_have_id_title_and_content(self):
        response = self.client.get("/posts/")
        for post in response.json['posts']:
            self.assertTrue(set(['id','title','content']).issubset(post))

