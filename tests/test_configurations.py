def config():
    return {
        "test_name":
        "test_sync",
        "tap_name":
        "tap-activecampaign",
        "type":
        "platform.activecampaign",
        "properties": {
            "start_date": "TAP_ACTIVECAMPAIGN_START_DATE",
            "api_url": "TAP_ACTIVECAMPAIGN_API_URL",
            "user_agent": "TAP_ACTIVECAMPAIGN_USER_AGENT",
        },
        "credentials": {
            "api_token": "TAP_ACTIVECAMPAIGN_API_TOKEN",
        },
        "bookmark": {
            "bookmark_dict": "users",
            "bookmark_key": "id",
            "bookmark_timestamp": "2020-05-11T21:30:43.303000Z"
        },
        "streams": {
            "contacts": {"id"},
            "automations": {"id"},
            "contact_automations": {"id"},
            "account_contacts": {"id"},
            "automation_blocks": {"id"},
            "saved_responses": {"id"},
            "account_custom_field_values": {"id"},
            "deal_custom_field_values": {"id"},
            "segments": {"id"},
            "ecommerce_connections": {"id"},
            "ecommerce_customers": {"id"},
            "deal_activities": {"id"},
            "contact_deals": {"id"},
            "tasks": {"id"},
            "conversions": {"id"},
            "deal_group_users": {"id"},
            "addresses": {"id"},
            "templates": {"id"},
            "groups": {"id"},
            "campaign_messages": {"id"},
            "deal_stages": {"id"},
            "contact_custom_field_options": {"id"},
            "conversion_triggers": {"id"},
            "contact_tags": {"id"},
            "contact_conversions": {"id"},
            "tags": {"id"},
            "webhooks": {"id"},
            "account_custom_fields": {"id"},
            "deal_custom_fields": {"id"},
            "accounts": {"id"},
            "deal_groups": {"id"},
            "messages": {"id"},
            "ecommerce_order_activities": {"id"},
            "calendars": {"id"},
            "contact_custom_field_rels": {"id"},
            "deals": {"id"},
            "sms": {"id"},
            "forms": {"id"},
            "brandings": {"id"},
            "email_activities": {"id"},
            "campaigns": {"id"},
            "lists": {"id"},
            "task_types": {"id"},
            "activities": {"id"},
            "contact_custom_fields": {"id"},
            "goals": {"id"},
            "configs": {"id"},
            "contact_custom_field_values": {"id"},
            "campaign_lists": {"id"},
            "campaign_links": {"id"},
            "users": {"id"},
            "contact_lists": {"id"},
            "scores": {"id"},
            "contact_data": {"id"},
            "contact_emails": {"id"},
            "ecommerce_orders": {"id"},
            "site_messages": {"id"},
            "bounce_logs": {"id"}
        },
        "exclude_streams": [
        ]
    }
