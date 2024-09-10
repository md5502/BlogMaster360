import random
import requests
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from blog.models import Post, Category, Tag, Comment

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        # Create some users
        users = []
        for _ in range(10):  # Create 5 fake users
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)

        # Create some categories
        categories = []
        for _ in range(20):  # Create 10 fake categories
            category = Category.objects.create(
                title=fake.word(),
                meta_title=fake.sentence(),
                body=fake.text(),
                owner=random.choice(users),
            )
            categories.append(category)

        # Create some tags
        tags = []
        for _ in range(15):  # Create 10 fake tags
            tag = Tag.objects.create(
                title=fake.word(),
                meta_title=fake.sentence(),
                body=fake.text(),
                owner=random.choice(users),
            )
            tags.append(tag)

        # Create some posts with images
        posts = []
        for _ in range(50):  # Create 20 fake posts
            post_image = self.download_image()  # Generate or download an image

            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                meta_title=fake.sentence(),
                body=fake.paragraph(nb_sentences=5),
                owner=random.choice(users),
                summary=fake.sentence(),
                image=post_image  # Assign the image
            )
            post.categories.add(*random.sample(categories, k=random.randint(1, 3)))
            post.tags.add(*random.sample(tags, k=random.randint(1, 3)))
            posts.append(post)

        # Create some comments
        for _ in range(100):  # Create 50 fake comments
            Comment.objects.create(
                body=fake.sentence(nb_words=12),
                owner=random.choice(users),
                post=random.choice(posts),
                approved_comment=fake.boolean()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data!'))

    def download_image(self):
        """
        Download or generate a random image for the post.
        This function downloads a random image from a free service like picsum.photos or placekitten.
        """
        image_url = fake.image_url(width=800, height=600)  # Use Faker's image URL generator
        image_response = requests.get(image_url)

        # Save image to 'uploads/' directory
        file_path = f"uploads/{fake.uuid4()}.jpg"
        with open(file_path, 'wb') as image_file:
            image_file.write(image_response.content)
        
        return file_path  # Return the image path for the Post model
