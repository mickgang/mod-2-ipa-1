def savings(gross_pay, tax_rate, expenses):
    return int(gross_pay - (gross_pay * tax_rate) - expenses)
    
savings(22234, 0.5, 3453)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    return str(total_material - (num_jobs * job_consumption)) + material_units

material_waste(3000, "kg", 30, 3)

def interest(principal, rate, periods):
    return int((principal * (rate * periods)) + principal)

interest(3000, 0.3, 3)

def body_mass_index(weight, height):
    return (weight / 2.205) / (((height[0] / 3.281) + (height[1] / 39.37)) ** 2)
    
body_mass_index(152, [5, 11])