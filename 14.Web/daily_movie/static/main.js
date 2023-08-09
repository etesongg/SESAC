document.addEventListener("DOMContentLoaded", function() {
    const span_texts = document.querySelectorAll("#text");
    span_texts.forEach(function(span_text) {
      const maxlen = 100; 
      const text = span_text.textContent;
      
      if (text.length > maxlen) {
        const truncatedText = text.substring(0, maxlen) + "...";
        span_text.textContent = truncatedText;
      }
    });
  });