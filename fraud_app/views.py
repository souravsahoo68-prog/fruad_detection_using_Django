from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import connection
from .models import Transaction
import pandas as pd
from django.contrib import messages
from django.db.models.functions import TruncMonth
from django.db.models import Count

@login_required
def index(request):
    total_txns = Transaction.objects.count()
    suspicious_count = Transaction.objects.filter(amount__gt=50000, transaction_type='Debit').count()

    monthly_data = (
        Transaction.objects.annotate(month=TruncMonth('timestamp'))
        .values('month').annotate(count=Count('transaction_id')).order_by('month')
    )
    months = [m['month'].strftime("%b %Y") for m in monthly_data]
    counts = [m['count'] for m in monthly_data]

    return render(request, 'fraud_app/index.html', {
        'total_txns': total_txns,
        'suspicious_count': suspicious_count,
        'months': months, 'counts': counts
    })

def transactions_list(request):
    qs = Transaction.objects.all()[:200]
    return render(request, 'fraud_app/transactions.html', {'transactions': qs})

def alerts(request):
    high_value = Transaction.objects.filter(amount__gt=50000, transaction_type='Debit')[:200]
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT customer_id, COUNT(*) AS failed_count
            FROM fraud_app_transaction WHERE status='Failed'
            GROUP BY customer_id HAVING failed_count>3 ORDER BY failed_count DESC LIMIT 50;
        """)
        rows = cursor.fetchall()
    failed_customers = [{'customer_id': r[0], 'failed_count': r[1]} for r in rows]
    df = pd.DataFrame(list(Transaction.objects.all().values('customer_id', 'amount')))
    plot_data = []
    labels = []
    data = []
    if not df.empty:
        grp = df.groupby('customer_id')['amount'].sum().reset_index().sort_values('amount', ascending=False).head(10)
        plot_data = grp.to_dict(orient='records')
        labels = grp['customer_id'].astype(str).tolist()
        data = grp['amount'].tolist()
    return render(request, 'fraud_app/alerts.html', {'high_value': high_value, 'failed_customers': failed_customers, 'plot_data': plot_data, 'labels':labels, 'data':data})

def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        try:
            df = pd.read_csv(csv_file)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            Transaction.objects.all().delete()
            records = [Transaction(
                transaction_id=int(r['transaction_id']),
                customer_id=int(r['customer_id']),
                amount=float(r['amount']),
                transaction_type=r.get('transaction_type', 'Debit'),
                timestamp=r['timestamp'],
                location=r.get('location', ''),
                merchant=r.get('merchant', ''),
                channel=r.get('channel', ''),
                status=r.get('status', 'Success')
            ) for _, r in df.iterrows()]
            Transaction.objects.bulk_create(records)
            messages.success(request, f"Uploaded {len(records)} rows successfully.")
        except Exception as e:
            messages.error(request, f"Upload failed: {e}")
        return redirect('fraud_app:transactions')
    return render(request, 'fraud_app/upload_csv.html')

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('fraud_app:index')  # redirect to dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'fraud_app/login.html', {'form': form})


from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')