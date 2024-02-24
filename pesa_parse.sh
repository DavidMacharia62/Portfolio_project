#!/bin/bash

# Array containing the M-PESA messages
messages=(
	
	"SAE01SX0NU Confirmed. Ksh130.00 paid to JOHN NJOROGE KAMAU. on 14/1/24 at 8:15 PM.New M-PESA balance is Ksh0.00. Transaction cost, Ksh0.00. Amount you can transact within the day is 499,620.00. To move money from bank to M-PESA, dial *334#>Withdraw>From bank to MPESA"
	
	"SAE91NNTJ9 Confirmed. Ksh70.00 sent to MARTIN  NJIRU 0720271531 on 14/1/24 at 7:41 PM. New M-PESA balance is Ksh0.00. Transaction cost, Ksh0.00. Amount you can transact within the day is 499,750.00. To reverse, foward this message to 456."
	
	"SAE5190USH Confirmed. Ksh100.00 sent to Kennedy  Wangari 0713496328 on 14/1/24 at 6:10 PM. New M-PESA balance is Ksh0.00. Transaction cost, Ksh0.00. Amount you can transact within the day is 499,820.00. To reverse, foward this message to 456."
	
	"SAE7175LQR Confirmed. Ksh50.00 sent to ELIJAH  MASILA 0702153662 on 14/1/24 at 5:57 PM. New M-PESA balance is Ksh0.00. Transaction cost, Ksh0.00. Amount you can transact within the day is 499,920.00. To reverse, foward this message to 456."
	
	"SAE6Z3RTE8 Confirmed. Ksh30.00 paid to Gregory Ndeto. on 14/1/24 at 12:13 PM.New M-PESA balance is Ksh0.00. Transaction cost, Ksh0.00. Amount you can transact within the day is 499,970.00. To move money from bank to M-PESA, dial *334#>Withdraw>From bank to MPESA"
	)

# Loop through the messages
for message in "${messages[@]}"; do
    echo "Enter the M-PESA message here: $message"
    ./parse_mpesa_message.py <<<"$message"
done

