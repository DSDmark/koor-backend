from rest_framework import serializers

from job_seekers.models import (
    EducationRecord, EmploymentRecord, Resume
)
from user_profile.models import JobSeekerProfile

from .backends import MobileOrEmailBackend as cb
from .models import User


class CreateUserSerializers(serializers.ModelSerializer):
    """
    CreateUserSerializer class provides serialization for creating a User model.

    The class extends the ModelSerializer from the rest_framework.serializers module. The Meta class
    specifies the model to use (User) and the fields to include in serialization.

    The validate_mobile_number method performs a custom validation on the mobile_number field. It ensures that the
    mobile_number is not blank and contains only numbers. In case of an error, it raises a ValidationError with a
    detailed error message.

    """

    class Meta:
        model = User
        fields = ['id', 'email', 'mobile_number', 'password', 'role', 'country_code']

    def validate_mobile_number(self, mobile_number):
        if mobile_number != '':
            if mobile_number.isdigit():
                try:
                    if User.objects.get(mobile_number=mobile_number):
                        raise serializers.ValidationError('mobile_number already in use.', code='mobile_number')
                except User.DoesNotExist:
                    return mobile_number
            else:
                raise serializers.ValidationError('mobile_number must contain only numbers', code='mobile_number')
        else:
            raise serializers.ValidationError('mobile_number can not be blank', code='mobile_number')

    def validate_email(self, email):
        if email != '':
            try:
                if User.objects.get(email=email):
                    raise serializers.ValidationError('email already in use.', code='email')
            except User.DoesNotExist:
                return email
        else:
            raise serializers.ValidationError('email can not be blank', code='email')

    def validate(self, data):
        country_code = data.get("country_code")
        mobile_number = data.get("mobile_number")
        if mobile_number and country_code in ["", None]:
            raise serializers.ValidationError({'country_code': 'country code can not be blank'})
        return data


class CreateSessionSerializers(serializers.Serializer):
    """
    Serializer for creating a session for a user.

    Fields:
        email (str): The email of the user (optional).
        mobile_number (str): The mobile number of the user (optional).
        password (str): The password of the user.

    Methods:
        validate_mobile_number(mobile_number): Validates the mobile number.
        validate_email(email): Validates the email.
        validate(data): Validates the user credentials.
    """

    email = serializers.CharField(
        style={"input_type": "text"},
        write_only=True,
        required=False,
        allow_blank=True
    )
    mobile_number = serializers.CharField(
        style={"input_type": "text"},
        write_only=True,
        required=False,
        allow_blank=True
    )
    password = serializers.CharField(
        style={"input_type": "text"},
        write_only=True
    )

    def validate_mobile_number(self, mobile_number):
        if mobile_number != '':
            if mobile_number.isdigit():
                try:
                    if User.objects.get(mobile_number=mobile_number):
                        return mobile_number
                except User.DoesNotExist:
                    raise serializers.ValidationError('mobile_number not exist.', code='mobile_number')
            else:
                raise serializers.ValidationError('mobile_number must contain only numbers', code='mobile_number')
        else:
            raise serializers.ValidationError('mobile_number can not be blank', code='mobile_number')

    def validate_email(self, email):
        if email != '':
            try:
                if User.objects.get(email=email):
                    return email
            except User.DoesNotExist:
                raise serializers.ValidationError('email not exist.', code='email')
        else:
            raise serializers.ValidationError('email can not be blank', code='email')

    def validate(self, data):
        email = data.get("email", "")
        mobile_number = data.get("mobile_number", "")
        password = data.get("password", "")
        user = None
        user_instance = None
        identifier = None
        try:
            if email:
                user_instance = User.objects.filter(email=email).filter(is_active=False)
                identifier = email
            elif mobile_number:
                user_instance = User.objects.filter(mobile_number=mobile_number).filter(is_active=False)
                identifier = mobile_number
            if user_instance.exists():
                raise serializers.ValidationError({'message': 'User not activate.'})
            else:
                user = cb.authenticate(self, identifier=identifier, password=password)
            if user:
                return user
            else:
                raise serializers.ValidationError({'message': 'Invalid login credentials.'})
        except:
            raise serializers.ValidationError({'message': 'Invalid login credentials.'})


class JobSeekerProfileSerializer(serializers.ModelSerializer):
    """
    JobSeekerProfileSerializer is a serializer class that serializes and deserializes the JobSeekerProfile model into
     JSON format.

    This serializer uses the Django Rest Framework's ModelSerializer class, which automatically generates fields based
    on the model.

    Attributes:
    model (JobSeekerProfile): The model that will be serialized.
    fields (tuple): The fields from the model that will be serialized.
    """

    class Meta:
        model = JobSeekerProfile
        fields = (
            'gender',
            'dob',
            'employment_status',
            'description',
            'market_information_notification',
            'job_notification'
        )


class EducationRecordSerializer(serializers.ModelSerializer):
    """
    EducationRecordSerializer is a serializer class that serializes and deserializes the EducationRecord model into
    JSON format.

    This serializer uses the Django Rest Framework's ModelSerializer class, which automatically generates fields
    based on the model.

    Attributes:
    model (EducationRecord): The model that will be serialized.
    fields (tuple): The fields from the model that will be serialized.
    """

    class Meta:
        model = EducationRecord
        fields = (
            'id',
            'title',
            'start_date',
            'end_date',
            'present',
            'organization',
            'description'
        )


class EmploymentRecordSerializer(serializers.ModelSerializer):
    """
    EmploymentRecordSerializer is a serializer class that serializes and deserializes the EmploymentRecord model into
     JSON format.

    This serializer uses the Django Rest Framework's ModelSerializer class, which automatically generates fields based
     on the model.

    Attributes:
    model (EmploymentRecord): The model that will be serialized.
    fields (tuple): The fields from the model that will be serialized.
    """
    class Meta:
        model = EmploymentRecord
        fields = (
            'id',
            'title',
            'start_date',
            'end_date',
            'present',
            'organization',
            'description'
        )


class ResumeSerializer(serializers.ModelSerializer):
    """
    ResumeSerializer is a serializer class that serializes and deserializes the Resume model into
     JSON format.

    This serializer uses the Django Rest Framework's ModelSerializer class, which automatically generates fields based
     on the model.

    Attributes:
    model (Resume): The model that will be serialized.
    fields (tuple): The fields from the model that will be serialized.
    """

    class Meta:
        model = Resume
        fields = (
            'id',
            'title',
            'file_path',
            'created_at'
        )