const mailElements = document.querySelectorAll('.mail');

mailElements.forEach(mailElement => {
   const senderButton = mailElement.querySelector('.button_sender');
   if (senderButton) {
		const senderEmail = senderButton.getAttribute('title');
        // 보낸 사람의 메일 주소가 newneek.co (indexOf 사용)
        if (senderEmail.indexOf('newneek.co') != -1) { 
            const checkbox = mailElement.querySelector('.button_checkbox_wrap input');
            checkbox.checked = true;
        }
   }
})