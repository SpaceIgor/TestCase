from django.utils.dateparse import parse_date
from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


@api_view(['GET'])
def list_expenses_by_date_range(request, user_id, start_date, end_date):
    start_date = parse_date(start_date)
    end_date = parse_date(end_date)
    expenses = Expense.objects.filter(user_id=user_id, date__range=[start_date, end_date])
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_summary(request, user_id, year, month):
    expenses = Expense.objects.filter(user_id=user_id, date__year=year, date__month=month)
    summary = expenses.values('category').annotate(total=Sum('amount'))
    return Response(summary)
