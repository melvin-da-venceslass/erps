#invoic_Writer
import fpdf
from PyPDF2 import PdfFileWriter, PdfFileReader
from num2words import num2words



overlay_pdf_file_name ="tempor.pdf"
pdf_template_file_name = 'Q_TEMP.pdf'

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


def q_writter(obj):
    
    pdf = fpdf.FPDF(format='A4', unit='pt')
    pdf.add_page()
    pdf.add_font('Montserrat Regular', '', 'Montserrat-Regular.ttf', uni=True)
    pdf.add_font('Montserrat Bold', '', 'Montserrat-SemiBold.ttf', uni=True)

    invoice_params = dict(obj)
    result_pdf_file_name = invoice_params["invoice_no"]

    panel_x = 40
    panel_y = 165
################
    #bill to Addres:
    pdf = title(pdf,invoice_params["name"],panel_x,panel_y,w=240,h=10)
    
    pdf = content(pdf,invoice_params["address_bill"],panel_x,panel_y+25,w=240,h=10)

    #ship to address
    pdf = title(pdf,"Kind Attn: " ,panel_x,panel_y+90,w=200,h=10,)
    pdf = content(pdf,invoice_params["atten"],panel_x+60,panel_y+90,w=200,h=10)

    #invoice_infos x =300
    panel_x = 287
    panel_y = 165
    panel_w=125

    pdf = title(pdf,invoice_params["invoice_no"],panel_x,panel_y,w=panel_w)
    pdf = title(pdf,invoice_params["leadtime"],panel_x,panel_y+35,w=panel_w,h=10,f=10)
    pdf = title(pdf,invoice_params["payment_mode"],panel_x,panel_y+73,w=panel_w,h=10,f=10)
    pdf = title(pdf,invoice_params["destination"],panel_x,panel_y+108,w=panel_w,h=10,f=10)

    panel_w=265
    pdf = title(pdf,invoice_params["payment_tearms"],panel_x,panel_y+145,w=panel_w,h=10,f=9)
    



    #x = 415
    panel_x=413
    panel_w=120
    
    pdf = title(pdf,invoice_params["invoice_date"],panel_x,panel_y,w=panel_w)
    pdf = title(pdf,invoice_params["validity"],panel_x,panel_y+35,w=panel_w)
    pdf = title(pdf,invoice_params["reference"],panel_x,panel_y+73,w=panel_w,h=10,f=10)
    pdf = title(pdf,invoice_params["dispatch_thru"],panel_x,panel_y+108,w=panel_w,h=10,f=10)


    #line item
    panel_y= 380
    pdf = title(pdf,invoice_params["line_item"],75,panel_y,w=150,h=10,f=9,a="L")
    pdf = title(pdf,invoice_params["hsn"],230,panel_y,w=55,h=10,f=9,a="L")
    pdf = title(pdf,invoice_params["item_gst"],285,panel_y,w=50,h=10,f=9,a="C")
    pdf = title(pdf,invoice_params["cost"],337,panel_y,w=70,h=10,f=9,a="R")
    pdf = title(pdf,invoice_params["qty"],405,panel_y,w=35,h=10,f=9,a="C")

    panel_x = 455

    pdf = title(pdf,invoice_params["t_cost"],panel_x,panel_y,w=100,h=10,f=9,a="R")

    panel_w = 100

    panel_y = 412
    pdf = title(pdf,invoice_params["gst_s_valu"],panel_x,panel_y,w=panel_w, h=10,f=9,a="R")
    pdf = title(pdf,invoice_params["gst_c_valu"],panel_x,panel_y+18,w=panel_w, h=10,f=9,a="R")
    pdf = title(pdf,invoice_params["gst_i_valu"],panel_x,panel_y+35,w=panel_w, h=10,f=9,a="R")

    pdf = title(pdf,invoice_params["gst_tot_value"],panel_x,panel_y+50,w=panel_w, h=10,f=9,a="R")
    pdf = title(pdf,invoice_params["round_off"],panel_x,panel_y+68,w=panel_w, h=10,f=9,a="R")
    pdf = title(pdf,invoice_params["st_value"],panel_x,panel_y+87,w=panel_w, h=10,f=9,a="R")

    pdf = content(pdf,invoice_params["item_desc"],75,420,w=150,h=10,f=9)



    #write in words

    #write in words
    #str_value = get_in_words(invoice_params["sub_total"])
    pdf = title(pdf,invoice_params["t_cost_words"],40,535,w=500,h=10,f=9,a="L",)

    pdf = title(pdf,invoice_params["delivery_tearms"],40,580,w=500,h=10,f=9,a="L",)


############



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
    output_pdf.write(open(invoice_params["invoice_no"]+ ".pdf", "wb"))
