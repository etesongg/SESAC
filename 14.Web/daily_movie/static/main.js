document.addEventListener("DOMContentLoaded", function() {
    var span_texts = document.querySelectorAll("#text");
    span_texts.forEach(function(span_text) {
      var maxlen = 100; 
      var text = span_text.textContent;
      
      if (text.length > maxlen) {
        var truncatedText = text.substring(0, maxlen) + "...";
        span_text.textContent = truncatedText;
      }
    });
  });