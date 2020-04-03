from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Category", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.url})

    def get_tests(self):
        return self.test_set.all()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Test(models.Model):
    name = models.CharField("Test", max_length=100)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    time = models.PositiveIntegerField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/".join(reversed(
            reverse("test_detail", kwargs={"slug": self.category.url, "next_slug": self.url}).split("/")))

    def get_questions(self):
        return self.question_set.all()

    def get_minutes(self):
        if len(str(int(self.time / 60)) + ":00") == 4:
            return "0" + str(int(self.time / 60)) + ":00"
        return str(int(self.time / 60)) + ":00"

    # def get_result(self, answer_set):
    #     test_questions = self.question_set.all()
    #     right_counter = 0
    #     for i in range(len(answer_set)):
    #         if test_questions[i].get_right_answer()[0].text == answer_set[i]:
    #             right_counter += 1
    #     return str(right_counter / len(answer_set)) + "%"

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"


class Question(models.Model):
    text = models.TextField("Question")
    image = models.ImageField("Image", upload_to="questions/", blank=True, null=True)
    test = models.ForeignKey(Test, verbose_name="Test", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()

    def get_right_answer(self):
        return self.answer_set.filter(is_right=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Answer(models.Model):
    text = models.TextField("Answer")
    image = models.ImageField("Image", upload_to="answers/", blank=True, null=True)
    is_right = models.BooleanField("Right")
    question = models.ForeignKey(Question, verbose_name="Question", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
