document.addEventListener('DOMContentLoaded', function() {
    var deleteButtons = document.querySelectorAll('.delete_button'); // 依照class篩選
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            alert('確認刪除？');
            // window.location.href = "{{ url_for('delete_article', article_id=article_id) }}";
            }
        );
    });
});
