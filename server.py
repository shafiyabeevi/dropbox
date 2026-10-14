
import dropbox
from tkinter import Tk, filedialog
import os

TOKEN = "sl.u.AGxgf3efqa_Fv6ExycHvy2Wq_opVex95wycf68e6dJNl28hUDUeibQqvdEniOz72_FWbeOrxm2pkK5bDXgcjtvUYzj6_sC3nH8tlxbswClLsPTGRXiEScsh2-QeoyaXriNcujqqnrcxBsAycOI8_Coec9t0pS-eFsMYj9cuwKDH2xjT4IeU42U-GP5MZb93xkCqJjf8Ni5V4JK4d-cP0i-Cp8aF4NW_StwnaVQaWXrfcWbn0lDgR0efFJrykP26XR-CK6drjbFFXLlUvi--yoc6UuQBYl3lG-YGkdD6ldXDlZsJ4dQZmgdPMOf0zgzi4ui7F4TSarxrWmThdr4RfIp3F8CZVCNzJXtsIzbj4fiE5ssjkij8oFzQlmo507q-L0VAL6IwBcU45qsEX-d7Slqa03kT4zz9BzEnNe2qdfLEBSFeTcsWBCi-P1O4SJ2qDmKrXHuu4dmGpjDMxAtAoZ-PLldWtB_hwwsq0eacSxbzu-l-lgCAlXYZANM9kGj9i4K4gqDicEzU4mUqN3Db9s_zZ3AGcBNmQi3Psfhuh6N9ZFUlkrxUZoyIOVzJCejlHAvwazU5FoqlWSXYyhvUSXTUcKR-HgQHDSKepMpqPOV1_IesdxfZ5pm4GBkTIAdJgwbrjOqxYbLl9IZ864U0ZZhXk2oHGD0UKHVVE1WAx1myxwZc7vLsXjifbs3atPcm9mfPYvBcsyAosHj9Z_QgyZ3FNWzj1CzsFYwgfrugM8eSPidvBO2AgI10gYmsVL5ugMyPnW9m5P64Yre_gsEf6pt57sRK47h94_3QMCungsG2qmwBAIh3W96IXHDKQeU-5EvJ2cGfLt2rXTyg_36TlEV_X08LMNHm5UJpHqcYoVi3_wfd4X9i0wbgjqFfyJusOEMUw5kORkMOxeJRT3700oI-RoeFSwD-_e292Rdp9lReLtWZNumR1O2zupghi8j5O0xM6GNTil4LBWA7pzaagK2rEeleUX3AvkX0WqND0Oj9qNv_ScM0wnJIhBfbMclmL2vbJsqhOTI41x0IdRwfDPlA4-vyTBfniZZGWovPj6s6LeMESzF61j2ntOh3QIAu7_3ASP0Iyr8bCAZpD3Z5ce1qqP-jLBwM368-4VsStN4rXaSy2hJQSFT2uf8BKG8RKfl0kdUkj3V1KZtdhjd6ZN9BFzcELBP7ACirw-rFh1jYQQ3X7kLzgYTM15T7laScQlTaitby_YJMu7sP0jx6SdOrLmcHxzWqP3M8Asv3eu-OWAuxX1fCZbswNELsYa_ErHAAElCrw3oYJxQZ-5gwYQQWMKLmhy98Gj-Dk50G-3gR_vIHHSr0A_-2H083Xmbx7ko7UFk2wdPf3vvUMC4jBIBRTch3-V1ZkIr1sr7nBCjSU0YKZAJLqqtKbewqdlwIty-XjvVWxZQ_DgxLm00OwXBzuIn0MW2iWhPB50qWOYL4zdsFCOpdAFGvX3Jf1v6slXL8"

Tk().withdraw()
file = filedialog.askopenfilename(
    title="Select a photo",
    filetypes=[("Image files", "*.png *.jpg *.jpeg")]
)

if file:
    dbx = dropbox.Dropbox(TOKEN)

    with open(file, "rb") as f:
        dbx.files_upload(
            f.read(),
            "/" + os.path.basename(file)
        )

    print("Photo uploaded successfully!")
else:
    print("No photo selected.")