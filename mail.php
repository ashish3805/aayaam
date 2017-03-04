<?php

$name = $_POST['name'];
$contact=$_POST['contact'];
$message=$_POST['message'];

date_default_timezone_set('Asia/Kolkata');
$time = date('m/d/Y h:i:s a', time());

echo $_POST['g-recaptcha-response']. " IS THE CAPTCHA RESPONSE ";

if(isset($_POST['g-recaptcha-response']) && !empty($_POST['g-recaptcha-response'])){
        //your site secret key
        $secret = '6LdUqxcUAAAAABu5at6UpmGbPSX1FBxhCmeWl1QZ';
        //get verify response data
        $verifyResponse = file_get_contents('https://www.google.com/recaptcha/api/siteverify?secret='.$secret.'&response='.$_POST['g-recaptcha-response']);
        $responseData = json_decode($verifyResponse);
        if($responseData->success){
            echo "its ok";
            $to = 'aayaamsgsits@gmail.com';
            $subject = 'Message From '.$name.' on aayaam.sgsits.ac.in';
            $header='From:aayaamsgsits@gmail.com' . "\r\n" .
               'Reply-To: no-reply@aayaam.sgsits.ac.in' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();
            $message=$message."\n".$contact;
            $send=mail($to,$subject,$message,$header);

            if($send)
                echo 'done';
            else
                echo 'false';
        }
        else echo "problem verifying response";
}
else 
    echo "not done"
?>
