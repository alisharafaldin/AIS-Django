

{// Start JS dalil_search
  document.addEventListener('DOMContentLoaded', function() {
    var citySelect = document.getElementById('city-select');
    
    // تحقق مما إذا كانت المدينة محددة بالفعل (من search_cityID)
    if (citySelect.value) {
        citySelect.options[0].text = citySelect.options[citySelect.selectedIndex].text;
    }
  });
  function goToCityPage() {
      var citySelect = document.getElementById('city-select');
      var selectedCityID = citySelect.value;
      // إنشاء رابط جديد بدون معايير استعلام سابقة
      var newURL = new URL(window.location.origin + window.location.pathname);
      // إضافة المدينة المختارة كمعيار استعلام
      newURL.searchParams.set('cityID', selectedCityID);
      // التوجيه إلى الرابط الجديد
      window.location.href = newURL.toString();
  }
      // End JS dalil_search
}
