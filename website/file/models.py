import datetime
import uuid
import shortuuid

from django.db import models
from django.contrib.auth.models import User

from shortuuidfield import ShortUUIDField


class File(models.Model):
    """Store a file on the website.
    Deleting file after 1 day by default."""

    file = models.FileField(upload_to="files", default="")
    name = models.CharField(max_length=255, unique=True, null=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="file_author"
    )
    description = models.TextField(null=True)

    # No permission needed to read
    public = models.BooleanField(default=True)

    # To delete file after use to free memory
    expiration = models.DurationField(default=datetime.timedelta(days=1), null=True)

    # descriptor = models.FileDescriptor(null=True)
    path = models.FilePathField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    written = models.DateTimeField(auto_now=True)
    read = models.DateTimeField(auto_now=True)

    read_count = models.PositiveIntegerField(default=0)
    write_count = models.PositiveIntegerField(default=0)

    def update_read(self):
        """Update file when user reads."""
        self.read_count += 1
        self.read = datetime.datetime.now()

    def update_write(self):
        """Update file when user reads."""
        self.write_count += 1
        self.written = datetime.datetime.now()

    # def


class PermissionChoices(models.TextChoices):
    """Permission type choices."""

    READ = "read"  # right to read
    WRITE = "write"  # right to write
    STAFF = "staff"  # right to write meta data
    ADMIN = "admin"  # rigth to add permissions


class Permission(models.Model):
    """User permission to access a file.

    Process:
        - Author of file create temporary access to permission
        - Permission available through public url (uuid based)
        - Connected user can click this url and get permission.
        - As soon as clicked the user is redirected to file.
    """

    permission = models.CharField(max_length=255, choices=PermissionChoices.choices)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    revoked = models.DateTimeField(null=True)


url_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~"


def get_uuid():
    return shortuuid.ShortUUID(alphabet=url_alphabet).random(6)


class Access(models.Model):
    """Temporary access to a file permission
    Available 1 hour by default.
    UUIDS are 6 characters long in a 66 characters long alphabet
    (all possible url characters not reserved)
    6 characters give 82653950016 possible access UUIDS ~= 10^12.
    Even with 6 characters the uuids is unguessable by modern computers.

    alphabet: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~"

    Default to one access count.
    """

    id = ShortUUIDField(
        primary_key=True,
        editable=True,
        default=get_uuid,
        max_length=6,
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    permission = models.CharField(
        max_length=255,
        choices=PermissionChoices.choices,
        default=PermissionChoices.READ,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    expiration = models.DurationField(default=datetime.timedelta(hours=1), null=True)
    count = models.PositiveIntegerField(default=0)
    max_count = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    def update(self):
        """Update counter when resources requested."""
        self.count += 1


class Token(models.Model):
    """Token for identifing user posting file."""

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    created = models.DateTimeField(auto_now_add=True)
