from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_env: str = Field("dev", env="APP_ENV")
    tz: str = Field("America/Santiago", env="TZ")

    # Database configuration
    database_url: str = Field(..., env="DATABASE_URL")

    # Meta configuration
    meta_app_id: str = Field(..., env="META_APP_ID")
    meta_app_secret: str = Field(..., env="META_APP_SECRET")
    meta_verify_token: str = Field(..., env="META_VERIFY_TOKEN")
    meta_page_access_token: str = Field(..., env="META_PAGE_ACCESS_TOKEN")
    meta_ig_business_id: str = Field(..., env="META_IG_BUSINESS_ID")
    meta_catalog_id: str = Field(..., env="META_CATALOG_ID")

    # WhatsApp configuration
    wa_phone_number_id: str = Field(..., env="WA_PHONE_NUMBER_ID")
    wa_business_account_id: str = Field(..., env="WA_BUSINESS_ACCOUNT_ID")
    wa_token: str = Field(..., env="WA_TOKEN")

    # Google Sheets configuration
    gcp_service_account_json_path: str = Field(
        "/app/creds/service_account.json", env="GCP_SERVICE_ACCOUNT_JSON_PATH"
    )
    google_sheets_inventory_key: str = Field(..., env="GOOGLE_SHEETS_INVENTORY_KEY")
    google_sheets_reports_key: str = Field(..., env="GOOGLE_SHEETS_REPORTS_KEY")

    # Notifications
    alert_emails: str = Field("", env="ALERT_EMAILS")
    smtp_host: str = Field("smtp.gmail.com", env="SMTP_HOST")
    smtp_port: int = Field(587, env="SMTP_PORT")
    smtp_user: str = Field(..., env="SMTP_USER")
    smtp_password: str = Field(..., env="SMTP_PASSWORD")

    # Feature toggles
    enable_ads: bool = Field(False, env="ENABLE_ADS")

    class Config:
        env_file = ".env"


settings = Settings()
