Library Project for Alx Django
Django Permissions & Groups Setup Guide

Define Custom Permissions: In your model’s Meta class, add custom permissions to tailor access as needed.

Create User Groups: Use the Django Admin to set up groups like Editors, Viewers, and Admins.

Assign Group Permissions: Through the admin interface, bind permission flags (e.g., can_view, can_create, can_edit, can_delete) to each group.

Enforce with Decorators: Protect your views by wrapping them with the @permission_required decorator to ensure only users with the necessary rights can access them.

Test the Setup: Create test users via the Django Admin, assign them to the pertinent groups, and verify that their view access is correctly restricted or granted.