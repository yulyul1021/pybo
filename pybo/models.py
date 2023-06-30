from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    subject         # 질문의 제목
    content         # 질문의 내용
    create_date     # 질문을 작성한 일시
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    """
    question        # 답변과 관련된 질문
    content         # 답변의 내용
    create_date     # 답변을 작성한 일시
    """
    # ForeignKey는 다른 모델과 연결하기 위해 사용
    # on_delete=models.CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우
    # 답변(Answer)도 함께 삭제된다는 의미
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')