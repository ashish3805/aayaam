<?php



$name = $_GET['name'];

$contact=$_GET['contact'];

$message=$_GET['message'];



date_default_timezone_set('Asia/Kolkata');

$time = date('m/d/Y h:i:s a', time());



$to = 'aayaamsgsits@gmail.com';

$subject = 'Message From '.$name.' on aayaam.sgsits.ac.in';

$header='From:aayaamsgsits@gmail.com' . "\r\n" .

   'Reply-To: no-reply@aayaam.sgsits.ac.in' . "\r\n" .

   'X-Mailer: PHP/' . phpversion();



$send=mail($to,$subject,$message,$header);



if($send)

	echo 'done';

else

	echo 'false';



?>
