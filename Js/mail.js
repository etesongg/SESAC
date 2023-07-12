const mailElements = document.querySelectorAll('.mail');

mailElements.forEach(mailElement => {
   const senderButton = mailElement.querySelector('.button_sender');
   if (senderButton) {
		const senderEmail = senderButton.getAttribute('title');
        // 보낸 사람의 메일 주소가 newneek.co (includes 사용)
        if (senderEmail.includes('newneek.co')) {
            const checkbox = mailElement.querySelector('.button_checkbox_wrap input[type="checkbox"]'); 
            // 클래스 이름이 button_checkbox_wrap인 요소 내부에 input 요소 중에서 type 속성 값이 checkbox인 요소. 
            // 네이버 메일에서는 button_checkbox_wrap input 까지만 쓰더라도 체크 가능
            checkbox.checked = true;
        }
   }
})