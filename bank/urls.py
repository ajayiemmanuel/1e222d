from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path ('about/', views.about, name = "about"),
    path ('contact/', views.contact, name = "contact"),
    path ('account-details/', views.account_details, name = "account-details"),
    path ('account/', views.account, name = "account"),
    path ('bill/', views.bill, name = "bill"),
    path ('business-loan/', views.business_loan, name = "business-loan"),
    path ('car-loan/', views.car_loan, name = "car-loan"),
    path ('card/', views.card, name = "card"),
    path ('cards/', views.cards, name = "cards"),
    path ('career-single/', views.career_single, name = "career-single"),
    path ('change-password/', views.change_password, name = "change-password"),
    path ('coin-details/', views.coin_details, name = "coin-details"),
    path ('pin-validation/', views.pin_validation, name = "pin-validation"),
    path ('crypto-send/', views.crypto_send, name = "crypto-send"),
    path ('crypto-transaction/', views.crypto_transaction, name = "crypto-transaction"),
    path ('crypto-view-transaction/', views.crypto_view_transaction, name = "crypto-view-transaction"),
    path ('crypto-withdraw/', views.crypto_withdraw, name = "crypto-withdraw"),
    path ('crypto/', views.crypto, name = "crypto"),
    path ('dashboard/', views.dashboard, name = "dashboard"),
    path ('educations-loan/', views.educations_loan, name = "educations-loan"),
    path ('forgot-password/', views.forgot_password, name = "forgot-password"),
    path ('help/', views.help, name = "help"),
    path ('home-loan/', views.home_loan, name = "home-loan"),
    path ('home/', views.home, name = "home"),
    path ('insight/', views.insight, name = "insight"),
    path ('login/', views.custom_login, name = "login"),
    path ('make-payment/', views.make_payment, name = "make-payment"),
    path ('my-account/', views.my_account, name = "my-account"),
    path ('my-portfolio/', views.my_portfolio, name = "my-portfolio"),
    path ('news-update-details/', views.news_update_details, name = "news-update-details"),
    path ('news-update/', views.news_update, name = "news-update"),
    path ('notification/', views.notification, name = "notification"),
    path ('otp/', views.otp, name = "otp"),
    path ('pay-successfully/', views.pay_successfully, name = "pay-successfully"),
    path ('personal-identity/', views.personal_identity, name = "personal-identity"),
    path ('personal-loan/', views.personal_loan, name = "personal-loan"),
    path ('preloader/', views.preloader, name = "preloader"),
    path ('privacy-policy/', views.privacy_policy, name = "privacy-policy"),
    path ('product/', views.product, name = "product"),
    path ('profile/', views.profile, name = "profile"),
    path ('register/', views.register, name = "register"),
    path ('reset-password/', views.reset_password, name = "reset-password"),
    path ('secure/', views.secure, name = "secure"),
    path ('service/', views.service, name = "service"),
    path ('setting/', views.setting, name = "setting"),
    path ('signin-successfully/', views.signin_successfully, name = "signin-successfully"),
    path ('successfully-signin/', views.successfully_signin, name = "successfully-signin"),
    path ('successfully-signup/', views.successfully_signup, name = "successfully-signup"),
    path ('terms-conditions/', views.terms_conditions, name = "terms-conditions"),
    path ('transaction-history/', views.transaction_history, name = "transaction-history"),
    path ('transfer/', views.transfer, name = "transfer"),
    path ('withdraw/', views.withdraw, name = "withdraw"),
    path('logout', views.custom_logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('template_activate_account', views.template_activate_account, name='template_activate_account'),
    path("change-password", views.change_password, name="change-password"),
    path("reset-password", views.reset_password, name="reset-password"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path ('pin/', views.pin, name = "pin"),

]