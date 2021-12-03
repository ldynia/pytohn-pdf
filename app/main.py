#!/usr/bin/env python3

import click

from datetime import datetime
from cert_generator import CertGenerator


@click.command()
@click.option('-bg', '--background', default='green', help='Background color')
@click.option('-fn', '--full-name', required=True, help='Full name user underscore as separator Jhon_Do')
@click.option('-d', '--date', default=datetime.now().strftime('%-d %B %Y'), help='Date')
@click.option('-u', '--uuid', help='UUID')
def generate_pdf(background, full_name, date, uuid):
    metadata = {
        'full_name': full_name.replace('_', ' '),
        'header': 'Course Certificate',
        'text': 'has seccessfully completed',
        'tilte': 'Basic Pharmacovigilance Test',
        'date': date,
        'background': background,
        'uuid': uuid,
    }
    pdf = CertGenerator(metadata=metadata, orientation='L', unit='mm', format='A4')
    pdf.output('/app/certs/test.pdf', 'F')


if __name__ == '__main__':
     generate_pdf()