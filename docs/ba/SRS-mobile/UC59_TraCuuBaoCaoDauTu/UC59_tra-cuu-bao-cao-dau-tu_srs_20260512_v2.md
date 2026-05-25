# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC59 — Tra cứu báo cáo đầu tư trên Mobile  
**Ngày tạo:** 12/05/2026  
**Phiên bản:** v2.5

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | hieu.luu2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Tra cứu thông tin báo cáo đầu tư |
| Đối tượng thực hiện | Nhà đầu tư, Người dùng chung (Cá nhân / Tổ chức) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 12/05/2026 |
| Phiên bản | v2.5 |

---

## UC59 — Tra cứu báo cáo đầu tư trên Mobile

### 1. Mô tả chức năng
- **Tên chức năng:** Tra cứu báo cáo đầu tư & Thông tin cơ quan ban hành.
- **Mô tả:** Chức năng cho phép người dùng tìm kiếm, lọc và xem chi tiết các báo cáo tình hình đầu tư (FDI, Đầu tư công...). Màn hình chi tiết hiển thị các chỉ số nổi bật (vốn, dự án mới, tăng trưởng), tóm tắt nội dung và mục lục báo cáo. Nút xem toàn bộ tài liệu (PDF) không được hiển thị trực tiếp bên ngoài, nhưng người dùng có thể xem trực tiếp nội dung từng phần bằng cách tương tác với Mục lục chính. Người dùng cũng có thể xem thông tin chi tiết của **Cơ quan ban hành**, bao gồm thông tin liên hệ và danh sách các tài liệu, thủ tục do cơ quan đó quản lý.
- **Phân quyền:** Public access (Không yêu cầu đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** Các hành động gọi app ngoại vi (Trình duyệt, Bản đồ, Trình gọi điện) chỉ kích hoạt Intent của OS, không tự vẽ UI bên trong App. Việc xem chi tiết nội dung thủ tục từ tab "Thủ tục quản lý" sẽ gọi sang giao diện của UC58.
- **Truy cập chức năng:** Trang chủ → "Báo cáo đầu tư".
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị danh sách báo cáo hoặc thông tin chi tiết cơ quan.
- **Chức năng đáp ứng usecase số:** UC59

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Báo cáo đầu tư

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại & Tiêu đề | Button (Icon) & Label | "Báo cáo đầu tư" | — | — | **Quy tắc hiển thị:** Header đỏ đậm, chữ trắng.<br>**Quy tắc hành động:** Tap icon (←) về màn trước (CMR-06). |
| 2 | Ô tìm kiếm & Bộ lọc | Searchbox & Button| "Tìm kiếm nhanh theo tên báo cáo, cơ quan ban hành" | x | — | **Quy tắc hiển thị:** Max length **255 ký tự** (CMR-01/G05).<br>**Quy tắc hành động:** Tìm kiếm có debounce 3s, trim khoảng trắng (CMR-01). Ô tìm kiếm áp dụng cho **toàn bộ lĩnh vực** (không chỉ tab đang chọn). Kết quả hiển thị trên tab "Tất cả" (CMR-01). Khi chuyển sang màn hình khác → Reset search/filter về trạng thái mặc định (CMR-01). Nút Bộ lọc nằm trong text box, mở Bottom Sheet (CMR-02). |
| 3 | Tab Group (Lĩnh vực) | Tab Group | "Tất cả" | — | — | **Quy tắc hiển thị:** Thanh tab ngang (Tất cả, FDI, Kinh tế vĩ mô, Báo cáo ngành, Chính sách...).<br>**Quy tắc hành động:** Chọn tab để lọc danh sách theo lĩnh vực tương ứng (đồng bộ với Dropdown Lĩnh vực trong Bộ lọc). |
| 4 | Thanh thông tin chung | Label | — | — | — | **Quy tắc hiển thị:** Hiển thị tổng số lượng báo cáo (VD: "5 báo cáo", khung đỏ chữ trắng) và Ngày cập nhật (VD: "Cập nhật: 12/05/2026"). |
| 5 | Danh sách Card báo cáo | List Card | — | — | — | **Quy tắc hiển thị:** Lazy load 20 item (CMR-04), tự động retry 3 lần khi lỗi (CMR-04). Pull to Refresh (CMR-13). Empty State "Không tìm thấy kết quả" (CMR-14). |
| 6 | Layout Thẻ Báo cáo | Card Box | — | — | — | **Quy tắc hiển thị:** Mỗi thẻ gồm:<br>- Icon PDF tài liệu (Màu sắc đa dạng: xanh, lục, cam, tím...).<br>- Tên báo cáo (In đậm).<br>- Icon tòa nhà & Tên cơ quan (VD: Cục Đầu tư nước ngoài).<br>- Icon lịch & Ngày phát hành (VD: 15/01/2026).<br>- Icon văn bản & Số trang, dung lượng (VD: 48 trang - 3.2 MB).<br>- Hashtag (VD: #Báo_cáo_năm, #FDI) trên nền xám nhạt.<br>- Nút "Xem chi tiết >" (nền trắng, chữ đỏ, viền đỏ). |
| 7 | Tương tác thẻ | Interaction | — | — | — | **Quy tắc hành động:** Tap vào toàn bộ thẻ hoặc nút "Xem chi tiết >" → Chuyển sang màn hình Chi tiết báo cáo. Áp dụng Debounce chống click double (CMR-18). |

---

#### 2.2 Bottom Sheet Bộ lọc tìm kiếm

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header Bộ lọc | Label | "Bộ lọc tìm kiếm" | — | — | Kèm đoạn text hướng dẫn: "Lọc để tìm báo cáo phù hợp..." nền cam nhạt. Căn giữa, nút X đóng. |
| 2 | Loại báo cáo | Dropdown | "Tất cả loại báo cáo" | x | — | Dropdown theo chuẩn CMR-03. Áp dụng D07: xóa hết keyword → hiển thị lại placeholder. Áp dụng D08: tap ra ngoài khi trống → chọn lại "Tất cả loại báo cáo". |
| 3 | Cơ quan ban hành | Dropdown | "Chọn cơ quan" | x | — | Dropdown theo chuẩn CMR-03. Áp dụng D07/D08: tap ra ngoài khi trống → chọn lại "Chọn cơ quan". |
| 4 | Năm phát hành | Dropdown | "Chọn năm" | x | — | Chọn theo dropdown năm thay vì Date Range Picker. Áp dụng D07/D08. |
| 5 | Lĩnh vực / Ngành | Dropdown | "Tất cả lĩnh vực" | x | — | Dropdown theo chuẩn CMR-03. Áp dụng D07/D08: tap ra ngoài khi trống → chọn lại "Tất cả lĩnh vực". |
| 6 | Nút Thiết lập lại / Áp dụng | Button | — | — | — | Nút "Thiết lập lại": Reset data. **Luôn Enabled** (I07).<br>Nút "Áp dụng": **Luôn Enabled** (I06). Tap → gọi API tìm kiếm theo filter. Khi đang gọi API → hiển thị loading state, disable tạm thời cho đến khi API trả về (I02). |

---

#### 2.3 Màn hình Chi tiết báo cáo

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header | Button & Label | "Chi tiết báo cáo" | — | — | Header đỏ đậm, chữ trắng. |
| 2 | Tag Phân loại | Badge | — | — | — | Giao diện: Chữ xanh trên nền xanh mờ (VD: "FDI / Đầu tư nước ngoài"). |
| 3 | Tiêu đề báo cáo | Label (H2) | — | — | — | In đậm, font lớn, chữ đen. |
| 4 | Thông tin phụ | Label | — | — | — | Số trang (VD: 48 trang) & Ngày ban hành (VD: 15/01/2026). |
| 5 | Khối Cơ quan ban hành | Card Button | — | — | — | **Quy tắc hiển thị:** Box viền đỏ mờ. Có icon, dòng "Cơ quan ban hành", Tên cơ quan (Cục Đầu tư nước ngoài — Bộ KH&ĐT) in đậm và icon mũi tên `>`.<br>**Quy tắc hành động:** Tap → Điều hướng sang màn hình **Thông tin cơ quan**. |
| 6 | Nhóm Hashtag | Tag Group | — | — | — | VD: `#Báo_cáo_năm`, `#FDI`. Nền xám nhạt bo góc tròn. |
| 7 | Khối Highlight Chỉ số | List Attribute | — | — | — | 3 cột chỉ số ngang nhau:<br>- **Vốn đăng ký** (Màu xanh dương đậm, VD: 38.23 tỷ USD).<br>- **Dự án mới** (Màu đen/đỏ thẫm, VD: 3.640).<br>- **Tăng trưởng** (Màu xanh lá, VD: +12.4%). Cần hiển thị dấu `+` / `-`. |
| 8 | Tóm tắt nội dung | Paragraph | — | — | — | Text giới thiệu nội dung báo cáo. Tự động giãn dòng vô tận nếu text quá dài. |
| 9 | Mục lục chính | List (Actionable) | — | — | — | Mỗi dòng có: Nút tròn đánh số thứ tự (màu đỏ mờ), Tên chương/mục lục, Số trang hiển thị căn lề phải (VD: Tr. 4).<br>**Quy tắc hành động:** Tap vào bất kỳ dòng nào → Hệ thống tự động mở trình đọc báo cáo (PDF Viewer) và nhảy ngay tới trang tương ứng của mục đó. |

---

#### 2.4 Màn hình Thông tin cơ quan
**Mô tả:** Truy cập từ link Cơ quan ban hành. Hiển thị Profile chung và 2 tab danh sách.

**Phần Profile (Header & Liên hệ):**
| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header | Button & Label | "Thông tin cơ quan" | — | — | Nền đỏ đậm, chữ trắng. |
| 2 | Logo & Tên cơ quan | Image & Label | — | — | — | Logo tròn ở giữa, viền đỏ mờ. Tên cơ quan in đậm (VD: Cục Đầu tư nước ngoài). Cơ quan chủ quản text nhỏ bên dưới. |
| 3 | Khối Hành động nhanh | Button Group | — | — | — | Gồm 3 nút tròn: Gọi điện, Website, Chỉ đường.<br>**Quy tắc hành động:** <br>- **Gọi điện:** Mở dialog trình quay số trên điện thoại (Không có sim vẫn mở và đẩy số sang được).<br>- **Website:** Mở trình duyệt web mặc định của thiết bị.<br>- **Chỉ đường:** Mở ứng dụng Google Maps. (Riêng trên iOS nếu không cài Google Maps thì fallback gọi Apple Maps). |
| 4 | Khối Thông tin liên hệ | List | — | — | — | Hiển thị 3 hàng: Địa chỉ, Điện thoại, Email (kèm icon tương ứng). Text cố định, không bấm. |

**Phần Tab Bar:**
| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 5 | Tab Bar (2 Tabs) | Tab Group | "Tài liệu phát hành" | — | — | 2 tab: "Tài liệu phát hành" và "Thủ tục quản lý". Hỗ trợ Swipe đổi tab trái/phải. |
| 6 | Tab "Tài liệu phát hành" | List Card | — | — | — | Header list hiển thị tổng số: "5 tài liệu" kèm Dropdown sort với 2 lựa chọn: **Mới nhất**, **Cũ nhất**.<br>Hiển thị danh sách các card Báo cáo y hệt như mô tả ở Mục 2.1. Hỗ trợ lazy load. |
| 7 | Tab "Thủ tục quản lý" | List Card | — | — | — | Hiển thị danh sách thẻ Thủ tục.<br>**Quy tắc hiển thị:** Layout có Tên thủ tục, Mã thủ tục, Lĩnh vực và Nút đỏ (VD: "Xem" / "Đóng").<br>**Quy tắc hành động:** Tap thẻ chuyển sang màn hình Chi tiết thủ tục (Gọi view của UC58). |

---

### 3. Mô tả các xử lý của chức năng

1. **Tìm kiếm & Lọc:**
   - Ô tìm kiếm gọi API với **debounce 3s** và tự động loại bỏ khoảng trắng (auto-trim theo CMR-01).
   - Bộ lọc theo Năm phát hành sử dụng Dropdown để dễ dùng, thay vì Calendar.
   - **Đồng bộ Lĩnh vực:** Tab Group Lĩnh vực ở ngoài màn hình chính và Dropdown Lĩnh vực trong Bottom Sheet phải hoạt động đồng bộ với nhau (khi chọn ở ngoài thì dropown ở trong tự cập nhật tương ứng và ngược lại).
2. **Xử lý số liệu Highlight (Chi tiết báo cáo):**
   - API trả về số thực, Mobile phải định dạng theo chuẩn hàng nghìn của CMR-11.
   - API trả về `%` tăng trưởng: Mobile tự xử lý thêm prefix `+` nếu giá trị dương và bôi màu xanh lá, prefix `-` nếu giá trị âm và bôi màu đỏ.
3. **Màn hình Thông tin cơ quan:**
   - Dữ liệu ở Tab "Tài liệu" và Tab "Thủ tục" tải độc lập bằng cơ chế **Lazy load 20 item** (CMR-04). Tự động retry 3 lần ngầm khi đứt mạng.
   - **Call Intent OS:**
     - Gọi điện: Gọi URL Scheme `tel://[điện_thoại]`. Hệ thống vẫn kích hoạt đẩy số sang màn hình Dialer kể cả khi không có SIM.
     - Website: Mở OS default browser (Chrome/Safari).
     - Chỉ đường: Query intent của Google Maps (Android/iOS). Nếu gọi thất bại (thiết bị iOS chưa cài đặt Google Maps), tự động fallback gọi intent của `maps://` (Apple Maps).
4. **Mở PDF Document:**
   - Việc mở nội dung Báo cáo (PDF) được trigger từ click vào Mục lục (Tab 1). Mobile App tích hợp PDF Viewer nội bộ, nhận params trang `page_number` để tự động cuộn đến đúng section khi mở file.
5. **State Persistence (CMR-01):**
   - Trạng thái cuộn list báo cáo và trạng thái của Bộ lọc phải được lưu giữ khi quay lại từ màn hình chi tiết.
6. **Partial API Failure (CMR-07):**
   - Ở màn Chi tiết hoặc màn Cơ quan, nếu block nào lỗi API (VD: không lấy được danh sách Tài liệu phát hành) thì block đó hiện Empty Error State, các phần Profile phía trên vẫn hiển thị bình thường.

---

### 4. Tiêu chí chấp nhận (AC)
- **AC1:** Các rule cốt lõi cho danh sách Báo cáo: Debounce 3s (CMR-01), Lazy Load 20 items (có tự retry - CMR-04), và State Persistence hoạt động đúng 100%.
- **AC2:** Lọc dữ liệu qua Bottom Sheet, trong đó trường "Năm phát hành" hiển thị list danh sách năm thay vì lịch chọn ngày.
- **AC3:** Ở màn hình Chi tiết, **Tap vào bất kỳ dòng Mục lục nào cũng sẽ mở báo cáo PDF và nhảy đúng tới số trang tương ứng**.
- **AC4:** Tại khối Highlight, `% Tăng trưởng` tự động sinh tiền tố `+` hoặc `-` và render đúng màu sắc (xanh/đỏ).
- **AC5:** Ở màn hình Cơ quan, 3 nút tương tác Gọi / Web / Chỉ đường hoạt động chính xác. (Test case: Chỉ đường trên máy iOS chưa cài Google Maps phải fallback qua Apple Maps. Thiết bị gọi điện không có SIM vẫn bung được màn hình quay số hiển thị đúng sdt).
- **AC6:** Tab Bar màn hình Cơ quan cho phép Swipe qua lại. Mỗi tab lazy load data một cách độc lập không làm treo giao diện. Cụm Dropdown sort "Mới nhất / Cũ nhất" hoạt động trơn tru.

---

### 5. Lịch sử cập nhật
| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 12/05/2026 | v1.0 | Tạo mới | (Không có) | Tạo mới tài liệu SRS UC59 | Phân tích từ 5 file design. Áp dụng CMR. Đính chính layout màn Danh sách. |
| 12/05/2026 | v2.0 | Giải quyết Gaps Audit | Chưa rõ logic đọc file PDF, sort danh sách và exception của Intent | - Thêm logic mở PDF từ Mục lục.<br>- Cập nhật Sort: Mới/Cũ nhất.<br>- Định nghĩa rõ Intent Gọi điện, Web, fallback Apple Maps. | Update theo trả lời QnA |
| 13/05/2026 | v2.0 → v2.1 | Cập nhật UI màn Danh sách | Ghi chú "nhầm layout thủ tục", Header không có chuông, Text search "Tìm kiếm báo cáo...", Layout thẻ card cũ | Bỏ ghi chú. Thêm Tab Lĩnh vực, Icon Chuông, Thanh đếm số lượng. Cập nhật layout thẻ card theo thiết kế mới. Đồng bộ filter Lĩnh vực. | Cập nhật theo hình ảnh UI mới do User cung cấp |
| 13/05/2026 | v2.1 → v2.2 | Giải quyết Gap Q5 | Header có Icon chuông nhưng chưa có hành động | Bổ sung quy tắc hành động: Tap Icon thông báo → Chuyển đến màn hình Danh sách Thông báo. | Theo yêu cầu làm rõ của Audit v3 |
| 21/05/2026 | v2.2 → v2.3 | Align CMR v6.0 — Ô tìm kiếm | Không khai báo max length | Bổ sung max length **255 ký tự** (CMR-01/G05) | Align theo Align_CMR_Mobile_20260520 v6.0 |
| 21/05/2026 | v2.2 → v2.3 | Align CMR v6.0 — Dropdown filter | Chỉ ghi "Dropdown theo chuẩn CMR-03" | Bổ sung D07 (clear keyword → placeholder) và D08 (tap ngoài khi trống → "Tất cả") | Align theo Align_CMR_Mobile_20260520 v6.0 |
| 21/05/2026 | v2.2 → v2.3 | Align CMR v6.0 — Nút Áp dụng / Thiết lập lại | Không ghi trạng thái enabled/disabled | Bổ sung: Luôn Enabled (I06, I07). Loading state khi gọi API (I02) | Align theo Align_CMR_Mobile_20260520 v6.0 |
| 21/05/2026 | v2.2 → v2.3 | Align CMR v6.0 — Empty State | `"Không tìm thấy kết quả."` (có dấu `.`) | `"Không tìm thấy kết quả"` (bỏ `.`) | Align theo Align_CMR_Mobile_20260520 v6.0 |
| 22/05/2026 | v2.3 → v2.4 | §2.1 — Phạm vi tìm kiếm (Tab) | Không mô tả search scope xuyên tab | Bổ sung: Ô tìm kiếm áp dụng cho toàn bộ lĩnh vực, kết quả hiển thị trên tab "Tất cả" (CMR-01) | Align CMR-01 rule "Phạm vi tìm kiếm (Tab)" |
| 22/05/2026 | v2.3 → v2.4 | §2.1 — Reset khi chuyển màn | Không mô tả | Bổ sung: Khi chuyển sang màn hình khác → Reset search/filter về trạng thái mặc định (CMR-01) | Align CMR-01 rule "Reset khi chuyển màn" |
| 22/05/2026 | v2.3 → v2.4 | §2.1 — Retry lazy load | Chỉ ghi "Lazy load 20 item (CMR-04)" | Bổ sung: Tự động retry 3 lần khi lỗi (CMR-04) | Align CMR-04 rule "Xử lý lỗi lazy load" |
| 23/05/2026 | v2.4 → v2.5 | §2.1 #1 — Xóa mô tả Icon thông báo | Row "Nút Quay lại, Tiêu đề & Icon thông báo" có mô tả icon chuông + hành động tap → Danh sách Thông báo | Đổi thành "Nút Quay lại & Tiêu đề", xóa mô tả icon thông báo | Icon thông báo là thành phần chung header, mô tả tập trung tại UC Thông báo |
