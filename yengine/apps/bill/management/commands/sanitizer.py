import logging
from optparse import make_option

from django.core.management import BaseCommand

from apps.bill.models import Signature
from apps.bill.filters import ImageConvertor, DotSignatureIdentifierProcessor

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--force',
            action='store_true',
            dest='force',
            default=False,
            help='Actually save the result to the database'),
        )

    def handle(self, *args, **options):
        if options['force'] is False:
            logger.warning(" !!! Not saving the results to the database. use the option --force for persistance.")

        convertor = ImageConvertor()

        # a typical threshold of 1% let us detect the dot-based signatures
        processor = DotSignatureIdentifierProcessor(threshold=0.01)

        # start by the new ones, for a fast and bright effect
        for s in Signature.objects.all().order_by('-id'):

            # if has already been sanitized
            if s.signature_image_data_url is None:
                continue

            # convert the base64 to an image object
            try:
                img = convertor.image_from_data_uri(s.signature_image_data_url)
            except ValueError:
                # clean the wrong format
                logger.info("clean format #{} {}".format(s.id, s))
                img = None
                s.signature_image_data_url = None
                if options['force'] is True:
                    s.save()

            if img is None:
                continue

            ratio = processor.get_colored_pixel_ratio(img)
            if ratio < processor.threshold:
                logger.info("clean dot signature #{} {}".format(s.id, s))
                s.signature_image_data_url = None
                if options['force'] is True:
                    s.save()
