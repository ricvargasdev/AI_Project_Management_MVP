from app.ai_client import AIClient
from app.database import SessionLocal
from app.services.project_service import ProjectService

from app.models.project import Project
from app.models.customer import Customer

db = SessionLocal()

db.query(Project).delete()
db.query(Customer).delete()
db.commit()

service = ProjectService(
    db=db,
    ai_client=AIClient()
)

#
# ---------------------------------------------------------
# MHP
# ---------------------------------------------------------
#

service.create_project(
    customer_name="MHP",
    title="Users API Improvements",
    document="""
    Meeting Date: 12 January 2026

    Summary:
    The customer requested additional information to be exposed through the Users API.

    Requirements:
    - Add customerType
    - Add startDate
    - Add accountStatus
    - Maintain backwards compatibility

    Notes:
    Existing API consumers must continue working without any changes.
    """
)

service.create_project(
    customer_name="MHP",
    title="Checkout Improvements",
    document="""
    Meeting Date: 25 January 2026

    Summary:
    Customer requested improvements to the checkout process.

    Requirements:
    - Stripe integration
    - Apple Pay support
    - Better payment error messages
    - Retry failed payments

    Notes:
    Replace the existing PayPal-only solution.
    """
)

service.create_project(
    customer_name="MHP",
    title="Reporting Dashboard",
    document="""
    Meeting Date: 8 February 2026

    Summary:
    Customer requested new management reports.

    Requirements:
    - Monthly sales dashboard
    - CSV export
    - Revenue by region
    - User activity charts

    Notes:
    Reports should be available only to managers.
    """
)

service.create_project(
    customer_name="MHP",
    title="Authentication Upgrade",
    document="""
    Meeting Date: 2 March 2026

    Summary:
    Customer requested stronger authentication.

    Requirements:
    - Multi-factor authentication
    - Password expiry
    - Login audit history

    Notes:
    Implementation must comply with company security policies.
    """
)

#
# ---------------------------------------------------------
# Philosopher Foods
# ---------------------------------------------------------
#

service.create_project(
    customer_name="Philosopher Foods",
    title="Shopify Migration",
    document="""
    Meeting Date: 5 February 2026

    Summary:
    Migration from WooCommerce to Shopify.

    Requirements:
    - Preserve product catalogue
    - Preserve SEO URLs
    - Redirect existing pages
    - Import customer accounts

    Notes:
    Migration must happen with minimal downtime.
    """
)

service.create_project(
    customer_name="Philosopher Foods",
    title="Amazon Marketplace Integration",
    document="""
    Meeting Date: 18 February 2026

    Summary:
    Customer wanted product synchronisation with Amazon.

    Requirements:
    - Inventory sync
    - Order import
    - Automatic price updates

    Notes:
    The integration should run every 15 minutes.
    """
)

service.create_project(
    customer_name="Philosopher Foods",
    title="Google Ads Optimisation",
    document="""
    Meeting Date: 10 March 2026

    Summary:
    Marketing team requested better Google Ads tracking.

    Requirements:
    - Conversion tracking
    - GA4 integration
    - Enhanced Ecommerce events

    Notes:
    Campaign performance should be visible inside GA4.
    """
)

#
# ---------------------------------------------------------
# Acme Ltd
# ---------------------------------------------------------
#

service.create_project(
    customer_name="Acme Ltd",
    title="Azure Active Directory Integration",
    document="""
    Meeting Date: 20 January 2026

    Summary:
    Customer requested Single Sign-On.

    Requirements:
    - Azure Active Directory
    - SAML authentication
    - Automatic user provisioning

    Notes:
    Employees should use their Microsoft accounts.
    """
)

service.create_project(
    customer_name="Acme Ltd",
    title="Mobile App Backend",
    document="""
    Meeting Date: 15 February 2026

    Summary:
    Backend APIs for a new mobile application.

    Requirements:
    - JWT authentication
    - Push notification support
    - User profile endpoints

    Notes:
    The mobile app will launch on iOS and Android.
    """
)

service.create_project(
    customer_name="Acme Ltd",
    title="Customer Portal",
    document="""
    Meeting Date: 22 March 2026

    Summary:
    Development of a customer self-service portal.

    Requirements:
    - View invoices
    - Download documents
    - Submit support tickets
    - Update account information

    Notes:
    The portal should support role-based permissions.
    """
)

db.close()

print("✅ Seed data loaded successfully.")