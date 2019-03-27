import click
from validate_email import validate_email
import datetime
import base58
import yaml


def validate_date(date):
    date_format = '%Y-%m-%d'
    try:
        datetime.datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def validate_type(iptype):
    type_list = ['Standard Track', 'Informational', 'Meta']
    if iptype not in type_list:
        raise Exception("Type Not in Type List. Please Enter a Valid Type From List: Standard Track | Informational | Meta")

def validate_status(status):
    status_list = ['Draft', 'Last Call', 'Accepted', 'Final (non-Core)', 'Final (Core)', 'Deferred']
    if status not in status_list:
        raise Exception("Status Not in Status List. Please Type a Valid Status From List: Draft | Last Call | Accepted | Final (non-Core) | Final (Core) | Deferred")


@click.command()
@click.option('--title', prompt='Please Enter A Title For Your StarIP', type=str)
@click.option('--author', prompt='Please Enter An Author Name For Your StarIP', type=str)
@click.option('--contact', prompt='Please Enter the Discussion Email For Your StarIP')
@click.option('--status', prompt='Please Select A Status From Available Options: Draft | Last Call | Accepted | Final (non-Core) | Final (Core) | Deferred')
@click.option('--iptype', prompt='Please Enter The Type For Your StarIP: Standard Track | Informational | Meta')
@click.option('--date', prompt='Please Enter A Date For Your StarIP In YYYY-MM-DD Format')
def preamble(title, author, contact, status, iptype, date):
    # Delete Title Start and Trailing White Spaces
    title = title.strip()

    # Delete Author Start and Trailing White Spaces
    author = author.strip()

    # Validate Email
    is_valid = validate_email(contact)
    if not is_valid:
        raise TypeError("Please Enter a Valid Email Address")
    contact = contact.strip()
    
    # Validate Status is Correct
    status = status.strip()
    validate_status(status)

    # Validate IP Type is Correct
    iptype = iptype.strip()
    validate_type(iptype)

    # Validate Date
    date = date.strip()
    validate_date(date)

    title_construct = f"Title: {title}\n"
    author_construct = f"Author: {author}\n"
    contact_construct = f"Discussions-To: {contact}\n"
    status_construct = f"Status: {status}\n"
    type_construct = f"Type: {iptype}\n"
    date_construct = f"Created: {date}"
    prehash_preamble = title_construct + author_construct + contact_construct + status_construct + type_construct + date_construct
    hashed_preamble = base58.b58encode(f"{prehash_preamble}")
    clean_hash = hashed_preamble.decode("utf-8") 
    ip_hash = clean_hash[-8:]
    readable_hash = clean_hash[-4:]
    starip_name = f"ECIP-{title}-{ip_hash}"

    preamble_dict = {
        'StarIP-Name': starip_name,
        'Reference-Hash': readable_hash,
        'Title': title,
        'Author': author,
        'Discussions-To': contact,
        'Status': status,
        'Type': iptype,
        'Created': date
    }
    stream = open('preamble.yaml', 'w')
    yaml.dump(preamble_dict, stream)
    click.echo("\n\nThe StarIP Preamble Has Been Generated:\n\n")
    print(yaml.dump(preamble_dict))
    click.echo("\n\nPreamble Has Been Saved to preamble.yaml File")


if __name__ == '__main__':
    click.echo('Welcome to the StarIP Preamble Generator! 🌟🌟🌟 \n\n')
    preamble()
