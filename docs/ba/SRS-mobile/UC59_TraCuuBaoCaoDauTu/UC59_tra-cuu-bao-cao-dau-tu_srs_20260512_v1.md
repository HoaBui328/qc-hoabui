# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC59 — Tra cứu báo cáo đầu tư trên Mobile  
**Ngày tạo:** 12/05/2026  
**Phiên bản:** v1.0

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | hieu.luu2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Tra cứu thông tin báo cáo đầu tư |
| Đối tượng thực hiện | Nhà đầu tư, Người dùng chung (Cá nhân / Tổ chức) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 12/05/2026 |
| Phiên bản | v1.0 |

---

## UC59 — Tra cứu báo cáo đầu tư trên Mobile

### 1. Mô tả chức năng
- **Tên chức năng:** Tra cứu báo cáo đầu tư & Thông tin cơ quan ban hành.
- **Mô tả:** Chức năng cho phép người dùng tìm kiếm, lọc và xem chi tiết các báo cáo tình hình đầu tư (FDI, Đầu tư công...). Màn hình chi tiết hiển thị các chỉ số nổi bật (vốn, dự án mới, tăng trưởng), tóm tắt nội dung và mục lục báo cáo. Người dùng cũng có thể xem thông tin chi tiết của **Cơ quan ban hành**, bao gồm thông tin liên hệ và danh sách các tài liệu, thủ tục do cơ quan đó quản lý.
- **Phân quyền:** Public access (Không yêu cầu đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** Hành động "Website" hoặc "Chỉ đường" ở màn hình Cơ quan sẽ mở trình duyệt/bản đồ của hệ điều hành. Việc xem chi tiết nội dung thủ tục từ tab "Thủ tục quản lý" sẽ gọi sang giao diện của UC58.
- **Truy cập chức năng:** Trang chủ → "Báo cáo đầu tư".
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị danh sách báo cáo hoặc thông tin chi tiết cơ quan.
- **Chức năng đáp ứng usecase số:** UC59

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Báo cáo đầu tư
*(Lưu ý: Thiết kế `Báo cáo đầu tư.png` gửi kèm đang hiển thị nhầm layout của phần "Thủ tục". Do đó, cấu trúc Card dưới đây được mô phỏng theo mẫu hiển thị ở tab "Tài liệu phát hành" - chuẩn cho UI danh sách báo cáo).*

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại & Tiêu đề | Button (Icon) & Label | "Báo cáo đầu tư" | — | — | **Quy tắc hiển thị:** Header đỏ đậm, chữ trắng. Tap icon (←) về màn trước (CMR-06). |
| 2 | Ô tìm kiếm & Bộ lọc | Searchbox & Button| "Tìm kiếm báo cáo..." | x | — | **Quy tắc hành động:** Tìm kiếm có debounce 3s, trim khoảng trắng (CMR-01). Nút Bộ lọc mở Bottom Sheet (CMR-02). |
| 3 | Danh sách Card báo cáo | List Card | — | — | — | **Quy tắc hiển thị:** Lazy load 20 item (CMR-04), Pull to Refresh (CMR-13). Empty State "Không tìm thấy kết quả" (CMR-14). |
| 4 | Layout Thẻ Báo cáo | Card Box | — | — | — | **Quy tắc hiển thị:** Mỗi thẻ gồm:<br>- Icon tài liệu màu đỏ.<br>- Tag loại báo cáo (VD: Báo cáo tháng, Thống kê - nền xanh dương nhạt).<br>- Tên báo cáo (In đậm).<br>- Ngày tháng (VD: 15/01/2026) & Số trang (VD: 48 trang).<br>- Nút "Xem" (nền đỏ đậm). |
| 5 | Tương tác thẻ | Interaction | — | — | — | **Quy tắc hành động:** Tap vào toàn bộ thẻ hoặc nút "Xem" → Chuyển sang màn hình Chi tiết báo cáo. Áp dụng Debounce chống click double (CMR-18). |

---

#### 2.2 Bottom Sheet Bộ lọc tìm kiếm

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header Bộ lọc | Label | "Bộ lọc tìm kiếm" | — | — | Kèm đoạn text hướng dẫn: "Lọc để tìm báo cáo phù hợp..." nền cam nhạt. Căn giữa, nút X đóng. |
| 2 | Loại báo cáo | Dropdown | "Tất cả loại báo cáo" | x | — | Dropdown theo chuẩn CMR-03. |
| 3 | Cơ quan ban hành | Dropdown | "Chọn cơ quan" | x | — | Dropdown theo chuẩn CMR-03. |
| 4 | Năm phát hành | Dropdown | "Chọn năm" | x | — | Chọn theo dropdown năm thay vì Date Range Picker. |
| 5 | Lĩnh vực / Ngành | Dropdown | "Tất cả lĩnh vực" | x | — | Dropdown theo chuẩn CMR-03. |
| 6 | Nút Thiết lập lại / Áp dụng | Button | — | — | — | Nút "Thiết lập lại": Reset data.<br>Nút "Áp dụng": Gọi API tìm kiếm theo filter. |

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
| 9 | Mục lục chính | List | — | — | — | Mỗi dòng có: Nút tròn đánh số thứ tự (màu đỏ mờ), Tên chương/mục lục, Số trang hiển thị căn lề phải (VD: Tr. 4). |

---

#### 2.4 Màn hình Thông tin cơ quan
**Mô tả:** Truy cập từ link Cơ quan ban hành. Hiển thị Profile chung và 2 tab danh sách.

**Phần Profile (Header & Liên hệ):**
| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header | Button & Label | "Thông tin cơ quan" | — | — | Nền đỏ đậm, chữ trắng. |
| 2 | Logo & Tên cơ quan | Image & Label | — | — | — | Logo tròn ở giữa, viền đỏ mờ. Tên cơ quan in đậm (VD: Cục Đầu tư nước ngoài). Cơ quan chủ quản text nhỏ bên dưới. |
| 3 | Khối Hành động nhanh | Button Group | — | — | — | Gồm 3 nút tròn: Gọi điện, Website, Chỉ đường.<br>**Quy tắc hành động:** Tap sẽ mở tính năng của OS (Gọi điện, Trình duyệt Web, Bản đồ). |
| 4 | Khối Thông tin liên hệ | List | — | — | — | Hiển thị 3 hàng: Địa chỉ, Điện thoại, Email (kèm icon tương ứng). Text cố định, không bấm. |

**Phần Tab Bar:**
| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 5 | Tab Bar (2 Tabs) | Tab Group | "Tài liệu phát hành" | — | — | 2 tab: "Tài liệu phát hành" và "Thủ tục quản lý". Hỗ trợ Swipe đổi tab trái/phải. |
| 6 | Tab "Tài liệu phát hành" | List Card | — | — | — | Header list hiển thị tổng số: "5 tài liệu" kèm dropdown sort "Mới nhất >".<br>Hiển thị danh sách các card Báo cáo y hệt như mô tả ở Mục 2.1. Hỗ trợ lazy load. |
| 7 | Tab "Thủ tục quản lý" | List Card | — | — | — | Hiển thị danh sách thẻ Thủ tục.<br>**Quy tắc hiển thị:** Layout có Tên thủ tục, Mã thủ tục, Lĩnh vực và Nút đỏ (VD: "Xem" / "Đóng").<br>**Quy tắc hành động:** Tap thẻ chuyển sang màn hình Chi tiết thủ tục (Gọi view của UC58). |

---

### 3. Mô tả các xử lý của chức năng

1. **Tìm kiếm & Lọc:**
   - Ô tìm kiếm gọi API với **debounce 3s** và tự động loại bỏ khoảng trắng (auto-trim theo CMR-01).
   - Bộ lọc theo Năm phát hành sử dụng Dropdown để dễ dùng, thay vì Calendar.
2. **Xử lý số liệu Highlight (Chi tiết báo cáo):**
   - API trả về số thực, Mobile phải định dạng theo chuẩn hàng nghìn của CMR-11.
   - API trả về `%` tăng trưởng: Mobile tự xử lý thêm prefix `+` nếu giá trị dương và bôi màu xanh lá, prefix `-` nếu giá trị âm và bôi màu đỏ.
3. **Màn hình Thông tin cơ quan:**
   - Dữ liệu ở Tab "Tài liệu" và Tab "Thủ tục" tải độc lập bằng cơ chế **Lazy load 20 item** (CMR-04). Tự động retry 3 lần ngầm khi đứt mạng.
   - **Call Intent OS:**
     - Gọi điện: Gọi Deeplink `tel://[điện_thoại]`
     - Website: Mở trình duyệt web.
     - Email: Mở ứng dụng Mail mặc định `mailto:[email]`
4. **State Persistence (CMR-01):**
   - Trạng thái cuộn list báo cáo và trạng thái của Bộ lọc phải được lưu giữ khi quay lại từ màn hình chi tiết.
5. **Partial API Failure (CMR-07):**
   - Ở màn Chi tiết hoặc màn Cơ quan, nếu block nào lỗi API (VD: không lấy được danh sách Tài liệu phát hành) thì block đó hiện Empty Error State, các phần Profile phía trên vẫn hiển thị bình thường.

---

### 4. Tiêu chí chấp nhận (AC)
- **AC1:** Các rule cốt lõi cho danh sách Báo cáo: Debounce 3s (CMR-01), Lazy Load 20 items (có tự retry - CMR-04), và State Persistence hoạt động đúng 100%.
- **AC2:** Lọc dữ liệu qua Bottom Sheet, trong đó trường "Năm phát hành" hiển thị list danh sách năm thay vì lịch chọn ngày.
- **AC3:** Màn hình Chi tiết báo cáo map đúng các block văn bản, xử lý tự động ngắt/giãn dòng nếu tóm tắt dài.
- **AC4:** Tại khối Highlight, `% Tăng trưởng` tự động sinh tiền tố `+` hoặc `-` và render đúng màu sắc (xanh/đỏ).
- **AC5:** Ở màn hình Cơ quan, 3 nút tương tác (Gọi, Web, Chỉ đường) gọi thành công Native App (Intent) của điện thoại.
- **AC6:** Tab Bar màn hình Cơ quan cho phép Swipe qua lại. Mỗi tab lazy load data một cách độc lập không làm treo giao diện.

---

### 5. Lịch sử cập nhật
| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 12/05/2026 | v1.0 | Tạo mới | (Không có) | Tạo mới tài liệu SRS UC59 | Phân tích từ 5 file design. Áp dụng CMR. Đính chính layout màn Danh sách. |
