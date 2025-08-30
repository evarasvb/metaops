from __future__ import annotations
from datetime import datetime
from typing import Dict, List
import smtplib
from email.mime.text import MIMEText

from .sheets_client import SheetsClient


class ReportingService:
    """
    Service for generating KPI reports and sending them to Google Sheets and via email.

    This class gathers key performance indicators (KPIs) from the system, writes them to a
    Google Sheet for record keeping, and sends a summary email to a list of recipients.
    """

    def __init__(
        self,
        sheets_client: SheetsClient,
        smtp_host: str,
        smtp_port: int,
        smtp_user: str,
        smtp_password: str,
        recipients: List[str],
    ) -> None:
        self.sheets_client = sheets_client
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.recipients = recipients

    def generate_kpi_row(self, kpis: Dict[str, int]) -> List[str]:
        """
        Build a row for the KPI sheet based on a dictionary of metrics.

        The date is automatically prepended.
        """
        date_str = datetime.now().strftime("%Y-%m-%d")
        return [
            date_str,
            str(kpis.get("posts", 0)),
            str(kpis.get("messages", 0)),
            str(kpis.get("comments", 0)),
            str(kpis.get("leads", 0)),
            str(kpis.get("errors", 0)),
        ]

    def append_to_sheet(self, sheet_key: str, worksheet_name: str, row: List[str]) -> None:
        """Append a row to a Google Sheet via the SheetsClient."""
        self.sheets_client.append_row(sheet_key, worksheet_name, row)

    def send_email(self, subject: str, body: str) -> None:
        """
        Send an email summary of the KPI report.

        Args:
            subject: Subject line for the email.
            body: Body text of the email.
        """
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.smtp_user
        msg["To"] = ", ".join(self.recipients)

        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.smtp_user, self.recipients, msg.as_string())

    def report_daily_kpis(
        self,
        sheet_key: str,
        worksheet_name: str,
        kpis: Dict[str, int],
        email_subject: str = "Daily KPI Report",
    ) -> None:
        """
        Generate a KPI row, append it to the sheet, and email a summary.

        Args:
            sheet_key: Google Sheet key for the KPI report.
            worksheet_name: Name of the worksheet/tab in the sheet.
            kpis: Dictionary of KPI metrics.
            email_subject: Optional subject for the email.
        """
        row = self.generate_kpi_row(kpis)
        self.append_to_sheet(sheet_key, worksheet_name, row)

        # Build email body
        lines = [f"{key.capitalize()}: {value}" for key, value in kpis.items()]
        body = "Daily KPI Report\n\n" + "\n".join(lines)
        self.send_email(email_subject, body)
