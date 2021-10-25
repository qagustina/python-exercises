# 1.7: La hipoteca de David
# 1.9: Calculadora de adelantos
# 1.10: Tablas

# 1.7
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

# 1.9 
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes_adelantado = 0 


while saldo > 0:
    
    saldo = saldo * (1+tasa/12)
    mes = mes + 1

    if (pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin):
        saldo = saldo - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        mes_adelantado = mes_adelantado + 1  

    else:
        saldo = saldo - pago_mensual
        total_pagado = total_pagado + pago_mensual 
    

    print(mes, round(total_pagado, 2), round(saldo, 2)) # 1.10 


print('Total pagado: ', round(total_pagado, ndigits=2))
print('Meses: ', mes)
print ('Meses adelantados: ', mes_adelantado)