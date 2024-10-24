document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // 기본 폼 제출 방지

    const type = document.getElementById('type').value; // 선택한 타입
    const input = document.querySelector('input[type="text"]').value; // 입력 값
    let apiUrl = '';

    // API URL 설정
    if (type === 'nm') {
        apiUrl = `/movies/${encodeURIComponent(input)}`; // 수정된 부분
    } else if (type === 'gn') {
        apiUrl = `/genres/${encodeURIComponent(input)}`; // 수정된 부분
    } else if (type === 'pn') {
        apiUrl = `/people/${encodeURIComponent(input)}`; // 수정된 부분
    }

    // API 호출
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('네트워크 응답이 좋지 않습니다.');
            }
            return response.json();
        })
        .then(data => {
            // 결과 처리 (콘솔에 출력)
            console.log(data);
            alert(JSON.stringify(data, null, 2)); // 데이터 표시
        })
        .catch(error => {
            console.error('문제가 발생했습니다:', error);
            alert('문제가 발생했습니다: ' + error.message);
        });
});
