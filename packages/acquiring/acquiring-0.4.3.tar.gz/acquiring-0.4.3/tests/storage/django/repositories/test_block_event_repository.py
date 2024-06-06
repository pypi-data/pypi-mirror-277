import uuid
from datetime import datetime

import pytest
from faker import Faker

from acquiring.enums import OperationStatusEnum
from acquiring.utils import is_django_installed
from tests.storage.utils import skip_if_django_not_installed

if is_django_installed():
    from acquiring import domain, storage
    from tests.storage.django.factories import PaymentAttemptFactory, PaymentMethodFactory

fake = Faker()


@skip_if_django_not_installed
@pytest.mark.django_db
@pytest.mark.parametrize("status", OperationStatusEnum)
def test_givenCorrectData_whenCallingRepositoryAdd_thenBlockEventGetsCreated(
    status: OperationStatusEnum,
) -> None:

    db_payment_method = PaymentMethodFactory(payment_attempt=PaymentAttemptFactory())
    block_event = domain.BlockEvent(
        created_at=datetime.now(),
        status=status,
        payment_method_id=db_payment_method.id,
        block_name="test",
    )

    result = storage.django.BlockEventRepository().add(db_payment_method.to_domain(), block_event)

    db_block_events = storage.django.models.BlockEvent.objects.all()
    assert len(db_block_events) == 1
    db_block_event = db_block_events[0]

    assert db_block_event.to_domain() == result


@skip_if_django_not_installed
@pytest.mark.django_db
@pytest.mark.parametrize("status", OperationStatusEnum)
def test_givenAllData_whenCallingRepositoryAdd_thenBlockEventGetsCreated(
    status: OperationStatusEnum,
) -> None:
    block_name = fake.name()

    db_payment_method = PaymentMethodFactory(payment_attempt=PaymentAttemptFactory())
    block_event = domain.BlockEvent(
        created_at=datetime.now(),
        status=status,
        payment_method_id=db_payment_method.id,
        block_name=block_name,
    )

    result = storage.django.BlockEventRepository().add(db_payment_method.to_domain(), block_event)

    db_block_event = storage.django.models.BlockEvent.objects.get(
        block_name=block_name, payment_method_id=db_payment_method.id, status=status
    )
    assert db_block_event.to_domain() == result


@skip_if_django_not_installed
@pytest.mark.django_db
def test_givenPaymentMethodWithDifferentIdThanTheOneStoredInBlockEvent_thenErrorGetsRaised() -> None:
    block_name = fake.name()

    db_payment_method = PaymentMethodFactory(payment_attempt=PaymentAttemptFactory())
    block_event = domain.BlockEvent(
        created_at=datetime.now(),
        status=OperationStatusEnum.PENDING,
        payment_method_id=uuid.uuid4(),
        block_name=block_name,
    )

    with pytest.raises(ValueError):
        storage.django.BlockEventRepository().add(db_payment_method.to_domain(), block_event)
