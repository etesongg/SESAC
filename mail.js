const mailElements = document.querySelectorAll('.mail');

mailElements.forEach(mailElement => {
   const senderButton = mailElement.querySelector('.button_sender');
   if (senderButton) {
		const senderEmail = senderButton.getAttribute('title');
        // 보낸 사람의 메일 주소가 newneek.co
        if (senderEmail.includes('newneek.co')) {
            const checkbox = mailElement.querySelector('.button_checkbox_wrap input[type="checkbox"]');
            checkbox.checked = true;
        }
    //     if (senderEmail.indexOf('newneek.co') != -1) { 
    //         console.log(senderEmail);
    //         // document.getElementById("wrap selection_mode").checked = true;
    // }
   }
})