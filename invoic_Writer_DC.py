
import fpdf,os

from PyPDF2 import PdfFileWriter, PdfFileReader
from num2words import num2words


overlay_pdf_file_name = "tempor.pdf"
pdf_template_file_name = "DC_TEMP.pdf"

def create_over(obj):
    obj.output(overlay_pdf_file_name)
    obj.close()
    return obj
    
def title(obj,msg,x,y,w=10,h=5,a="L",f=10,b=0):
    obj.set_font('Montserrat Bold', '', f)
    obj.set_xy(x,y)
    obj.multi_cell(w=w,h=h,align=a,txt=msg,border=b)
    return obj

def content(obj,msg,x,y,w=10,h=5,a="L",f=9,b=0):
    obj.set_font('Montserrat Regular', '', f)
    obj.set_xy(x,y)
    obj.multi_cell(w=w,h=h, align=a, txt=msg,border=b)
    return obj


def dc_writter(obj):
    
    pdf = fpdf.FPDF(format='A4', unit='pt')
    pdf.add_page()
    pdf.add_font('Montserrat Regular', '', 'Montserrat-Regular.ttf', uni=True)
    pdf.add_font('Montserrat Bold', '', 'Montserrat-SemiBold.ttf', uni=True)

    result_pdf_file_name = obj.invoice_no
    invoice_params = dict(obj)



    #bill to Addres:
    pannel_x = 40
    pannel_y = 165
    pdf = title(pdf,invoice_params["name"],pannel_x,pannel_y,w=240,h=10)
    pdf = content(pdf,invoice_params["address_bill"],pannel_x,pannel_y+25,w=240,h=10)

    #ship to address
    pdf = title(pdf,invoice_params["name_ship"],pannel_x,pannel_y+100,h=10,w=240)
    pdf = content(pdf,invoice_params["address_ship"],pannel_x,pannel_y+125,w=240,h=10)
    pdf = title(pdf,"Kind Attn: " ,pannel_x,pannel_y+160,w=200,h=10,)
    pdf = content(pdf,invoice_params["atten"],100,pannel_y+160,w=200,h=10)

    #invoice_infos x =300
    panel_x = 285

    panel_w=115

    pdf = title(pdf,invoice_params["delivery_note"],panel_x,160,w=panel_w,h=10,f=10)
    pdf = title(pdf,invoice_params["p_order"],panel_x,195,w=panel_w,h=10,f=10)
    pdf = title(pdf,invoice_params["dispatch_thru"],panel_x,230,w=panel_w,h=10,f=10)

    panel_x = 410
    pdf = title(pdf,invoice_params["deliver_on"],panel_x,160,w=panel_w,h=10,f=10)
    pdf = title(pdf,invoice_params["p_date"],panel_x,195,w=panel_w)
    pdf = title(pdf,invoice_params["destination"],panel_x,230,w=panel_w,h=10,f=10)


    panel_w=245
    panel_x = 290
    pdf = title(pdf,invoice_params["delivery_tearms"],panel_x,270,w=panel_w,h=10,f=9)
 


    #line item
    panel_y= 380
    panel_w=400
    pdf = title(pdf,invoice_params["line_item"],90,panel_y,w=panel_w,h=10,f=9,a="L")
    pdf = content(pdf,invoice_params["item_desc"],90,400,w=panel_w,h=10,f=9)
    pdf = title(pdf,invoice_params["qty"],500,panel_y,w=60,h=10,f=9,a="C")
    pdf = title(pdf,invoice_params["qty"],500,540,w=60,h=10,f=9,a="C")
    

    

    
    pdf = create_over(pdf)


    # Take the PDF you created above and overlay it on your template PDF
    # Open your template PDF
    pdf_template = PdfFileReader(open(pdf_template_file_name, 'rb'))
    # Get the first page from the template
    template_page = pdf_template.getPage(0)

    # # Open your overlay PDF that was created earlier
    overlay_pdf = PdfFileReader(open(overlay_pdf_file_name, 'rb'))

    # # Merge the overlay page onto the template page
    template_page.mergePage(overlay_pdf.getPage(0))


    # Write the result to a new PDF file
    output_pdf = PdfFileWriter()
    output_pdf.addPage(template_page)
    output_pdf.write(open(invoice_params["delivery_note"]+ ".pdf", "wb"))



