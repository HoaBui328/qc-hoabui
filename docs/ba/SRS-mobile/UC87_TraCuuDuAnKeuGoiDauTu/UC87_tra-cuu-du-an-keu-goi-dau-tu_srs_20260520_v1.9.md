# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile  
**Ngày tạo:** 20/05/2026  
**Tác giả:** Agent 6 (Mobile FDD Architect)  
**Phiên bản:** v1.9

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | han.luong & huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Khai thác thông tin xúc tiến đầu tư |
| Đối tượng thực hiện | Cá nhân / Tổ chức (Logged-in) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 20/05/2026 |
| Phiên bản | v1.9 |

---

## UC87 — Tra cứu dự án kêu gọi đầu tư trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu dự án kêu gọi đầu tư trên Mobile
- **Mô tả:** Chức năng cho phép nhà đầu tư (cá nhân/tổ chức) bổ sung thông tin nhu cầu đầu tư, nhận gợi ý dự án phù hợp thông qua matching tự động, tra cứu danh sách dự án kêu gọi đầu tư, và đăng ký quan tâm dự án.
- **Phân quyền:** Người dùng đã đăng nhập (Cá nhân / Tổ chức). Khách vãng lai KHÔNG truy cập được. Cá nhân và Tổ chức có cùng giao diện và chức năng, không phân biệt. Trường hợp Token chứa vai trò (role) không hợp lệ (ngoài 3 role trên) → Hệ thống xử lý như lỗi session hết hạn 401 theo quy định CMR-07 (không cho phép truy cập).
- **Phạm vi ngoài UC (Exclusions):** UC87 KHÔNG bao gồm: NĐT tự đề xuất dự án (thuộc phân hệ XTĐT), quản lý/phê duyệt dự án phía Admin, tra cứu CT XTĐT Quốc gia (UC88), tra cứu văn bản MOU (UC91).
- **Truy cập chức năng:** Sidebar → Mục **"Xúc tiến đầu tư"** → Chọn **"Dự án kêu gọi đầu tư"**
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định, người dùng đã đăng nhập vào hệ thống.
- **Điều kiện kết thúc (Postconditions):** 
  - (a) Sau khi bổ sung thông tin → Thông tin nhu cầu đầu tư của NĐT được lưu trên hệ thống, kết quả matching realtime trả về danh sách đề xuất phù hợp.
  - (b) Sau khi đăng ký quan tâm → Trạng thái đăng ký được lưu trên server, nút chuyển đổi thành "Hủy quan tâm" và đồng bộ trạng thái giữa màn hình Danh sách & Chi tiết.
  - (c) Sau khi hủy quan tâm → Trạng thái đăng ký bị xóa khỏi hệ thống, nút chuyển đổi lại thành "Đăng ký quan tâm".
- **Chức năng đáp ứng usecase số:** UC87 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình chính — Hub Dự án kêu gọi đầu tư (Tham chiếu: UC87 - Onboard.png)

**Mô tả giao diện:**
Header đỏ đậm "Dự án kêu gọi đầu tư" với nút Quay lại. Phần thân gồm 2 khối chức năng chính dạng Card lớn, xếp dọc: (1) Bổ sung thông tin NĐT - Gợi ý dự án phù hợp, (2) Danh sách dự án đề xuất.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về màn hình trước. (Xem CMR-06) |
| 2 | Tiêu đề Header | Label | "Dự án kêu gọi đầu tư" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, nằm giữa header, nền đỏ đậm. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | **Quy tắc hiển thị:**<br>- Icon chuông trắng + Badge dạng dot vàng (không hiển thị số) khi có thông báo mới. Không có thông báo mới → ẩn dot.<br>**Quy tắc hành động:**<br>- Tap → Điều hướng đến Trung tâm thông báo (UC riêng).<br>- Debounce Navigation (CMR-18). |
| 4 | Card "Bổ sung thông tin NĐT" | Card (Navigation) | — | — | — | **Quy tắc hiển thị:**<br>- Nền trắng, bo góc, shadow nhẹ. Icon minh họa + Tiêu đề "Bổ sung thông tin nhà đầu tư - Gợi ý dự án phù hợp" + Mô tả ngắn.<br>- Nút **"Cập nhật"** nằm trong card.<br>**Quy tắc hành động:**<br>- Tap card hoặc tap nút "Cập nhật" → Điều hướng đến Màn hình 2.2 (Bổ sung thông tin NĐT).<br>- Debounce Navigation (CMR-18). |
| 5 | Card "Danh sách dự án đề xuất" | Card (Navigation) | — | — | — | **Quy tắc hiển thị:**<br>- Nền trắng, bo góc, shadow nhẹ. Icon danh sách + Tiêu đề "Danh sách dự án đề xuất cho nhà đầu tư" + Mô tả ngắn.<br>- Nút **"Xem danh sách"** nằm trong card.<br>**Quy tắc hành động:**<br>- Tap card hoặc tap nút "Xem danh sách" → Điều hướng đến Màn hình 2.3 (Danh sách dự án đề xuất).<br>- Debounce Navigation (CMR-18). |

---
#### 2.2 Màn hình Bổ sung thông tin NĐT — Gợi ý dự án phù hợp (Tham chiếu: UC87 - Bổ sung thông tin.png)

**Mô tả giao diện:**
Màn hình form cho phép NĐT bổ sung nhu cầu đầu tư và thông tin quan tâm. Nếu NĐT đã bổ sung trước đó, form hiển thị thông tin đã điền (cho phép sửa). Sau khi bổ sung đầy đủ, NĐT nhấn "Xem dự án phù hợp" → hệ thống matching tự động (realtime) → hiển thị danh sách dự án phù hợp.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về Hub (2.1). (CMR-06) |
| 2 | Tiêu đề Header | Label | "Bổ sung thông tin" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, giữa header. |


**Khung Form bổ sung thông tin:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Lĩnh vực quan tâm | Dropdown (Multi-select) | "Tất cả" | x | x | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả".<br>- Cho phép chọn nhiều lĩnh vực, không giới hạn số lượng. Danh sách từ API danh mục. Searchable (CMR-03).<br>- Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa.<br>**Quy tắc hành động:**<br>- Inline error nếu bỏ trống: "Vui lòng chọn lĩnh vực quan tâm" (CMR-03) |
| 4 | Ngành kinh tế | Dropdown (Multi-select) | "Tất cả" | x | — | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả". Searchable (CMR-03).<br>- Không giới hạn số lượng. Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa. |
| 5 | Địa bàn mong muốn | Dropdown (Multi-select) | "Tất cả" | x | x | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả". Danh sách 63 tỉnh/TP. Searchable (CMR-03).<br>- Không giới hạn số lượng. Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa.<br>- Inline error nếu bỏ trống: "Vui lòng chọn địa bàn mong muốn" (CMR-03). |
| 6 | Hình thức đầu tư | Dropdown | "Tất cả" | x | — | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả".<br>- Giá trị: Tất cả / 100% vốn nước ngoài / Liên doanh / Hợp đồng BCC / Khác. |
| 7 | Quy mô vốn dự kiến | Textbox (Number) | — | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Nhập quy mô vốn dự kiến".<br>- Chỉ nhập số nguyên dương > 0 (không chấp nhận số âm, số 0 hay ký tự đặc biệt). Đơn vị: VNĐ (cố định, hiển thị label bên phải textbox).<br>- Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11).<br>- Tối đa 500 ký tự.<br>- Message lỗi validation nếu nhập <= 0: "Quy mô vốn dự kiến phải lớn hơn 0" (CMR-11).<br>- Message lỗi Max length: "Quy mô vốn dự kiến nhập quá ký tự cho phép" (CMR-09). |
| 8 | Quốc gia mong muốn hợp tác | Dropdown (Multi-select) | "Tất cả" | x | — | **Quy tắc hiển thị:**<br>- Giá trị mặc định: "Tất cả". Danh sách quốc gia từ API. Searchable (CMR-03).<br>- Không giới hạn số lượng. Hiển thị dạng chip/tag, wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa. |
| 9 | Mô tả nhu cầu đầu tư | Textarea | — | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Nhập mô tả nhu cầu đầu tư".<br>- Tối đa 2000 ký tự. Auto-trim whitespace (CMR-09).<br>- Message lỗi Max length: "Mô tả nhu cầu đầu tư nhập quá ký tự cho phép" (CMR-09). |
| 10 | Nút "Xem dự án phù hợp" | Button (Primary) | — | — | — | **Quy tắc hiển thị:**<br>- Disabled khi chưa điền đủ trường bắt buộc (CMR-09).<br>**Quy tắc hành động:**<br>- Tap → Hệ thống lưu thông tin NĐT + gọi API matching → Hiển thị kết quả matching (danh sách dự án phù hợp) tại Màn hình 2.3. |

---

#### 2.3 Màn hình Danh sách dự án đề xuất cho nhà đầu tư (Tham chiếu: UC87 - Dự án đề xuất.png, UC87 - Chưa có gợi ý.png, UC87 - Dự án đề xuất - Empty state.png)

**Mô tả giao diện:**
Màn hình danh sách các dự án phù hợp (matching tự động + gán thủ công bởi cơ quan quản lý). Có thanh tìm kiếm + bộ lọc nâng cao. NĐT có thể đăng ký quan tâm dự án từ danh sách.

**Trạng thái đặc biệt — NĐT chưa bổ sung thông tin:**
Nếu NĐT chưa từng bổ sung thông tin nhu cầu đầu tư (chưa thực hiện Chức năng 1), màn hình hiển thị danh sách rỗng kèm thông báo: *"Vui lòng bổ sung thông tin để nhận gợi ý dự án phù hợp."* và nút **"Bổ sung ngay"** (tap → điều hướng đến Màn hình 2.2). (Tham chiếu: UC87 - Chưa có gợi ý.png)

**Trạng thái đặc biệt — Danh sách rỗng (Không có dữ liệu):**
Nếu hệ thống matching không trả về kết quả hoặc khi kết quả tìm kiếm/lọc rỗng, màn hình hiển thị hình ảnh trống cùng thông báo: *"Không có dữ liệu."* (Tham chiếu: UC87 - Dự án đề xuất - Empty state.png, áp dụng CMR-14).

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về Hub (2.1). (CMR-06) |
| 2 | Tiêu đề Header | Label | "Dự án đề xuất" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, giữa header. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Ô tìm kiếm | Textbox (Search) | — | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Tìm kiếm nhanh theo tên dự án, mã dự án". Icon kính lúp bên trái. Tối đa 500 ký tự (CMR-01).<br>**Quy tắc hành động:**<br>- Debounce 3 giây (CMR-01). Tìm theo Tên dự án, Mã dự án.<br>- Auto-trim whitespace (CMR-01). |
| 4 | Nút Lọc | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Mở Bottom Sheet bộ lọc nâng cao.<br>- Active filter indicator (CMR-02). |

**Danh sách Dự án (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 5 | Thẻ dự án (Card) | Container | — | — | — | **Quy tắc hiển thị:**<br>- Khung trắng, bo góc, shadow nhẹ. Lazy load 20 bản ghi/lần (CMR-04).<br>- Hỗ trợ Pull to Refresh (CMR-13).<br>**Quy tắc hành động:**<br>- Tap card → Điều hướng đến Màn hình 2.4 (Chi tiết dự án). Debounce Navigation (CMR-18). |
| 6 | Tên dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm (H2), màu đen. Tối đa 2 dòng, truncate `...`. |
| 7 | Lĩnh vực | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon ngành + Tên lĩnh vực. |
| 8 | Địa bàn | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon định vị + Tên tỉnh/TP hoặc KCN. |
| 9 | Tổng vốn đầu tư dự kiến | Icon + Label | — | — | — | **Quy tắc hiển thị:**<br>- Icon $ + Số tiền (màu đỏ). Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11). |
| 10 | Ngày đăng ký | Label | — | — | — | **Quy tắc hiển thị:**<br>- Format: dd/MM/yyyy (CMR-12). Font nhỏ, màu xám. |
| 11 | Nút "Đăng ký quan tâm" / "Hủy quan tâm" | Button (Primary/Secondary, Small) | — | — | — | **Quy tắc hiển thị:**<br>- Trạng thái mặc định: "Đăng ký quan tâm" (nền đỏ, text trắng).<br>- Sau khi đăng ký thành công: Đổi thành "Hủy quan tâm" (nền trắng, viền xám, text xám).<br>- **Loading state:** Khi đang chờ API → button disabled + hiển thị spinner cục bộ thay text (CMR-07). Sau khi API trả về → khôi phục trạng thái tương ứng.<br>**Quy tắc hành động:**<br>- Tap "Đăng ký quan tâm" → API đăng ký → Toast "Đăng ký quan tâm thành công." → Đổi trạng thái nút.<br>- Tap "Hủy quan tâm" → API hủy → Toast "Đã hủy đăng ký quan tâm." → Đổi lại trạng thái nút.<br>- Không giới hạn số dự án đăng ký quan tâm.<br>- Debounce (CMR-18). |

**Modal Bottom Sheet — Bộ lọc nâng cao (Tham chiếu: UC87 - Filter dự án.png):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 15 | Nút X (Đóng) | Button (Icon) | — | — | — | Đóng Bottom Sheet, không thay đổi kết quả (CMR-02). |
| 16 | Loại dự án | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Tất cả / Trong nước / Nước ngoài / Trong & ngoài nước. |
| 17 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Searchable (CMR-03). |
| 18 | Ngành kinh tế | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Searchable (CMR-03). |
| 19 | Địa bàn (Tỉnh/TP) | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". 63 tỉnh/TP. Searchable (CMR-03). |
| 20 | Hình thức đầu tư | Dropdown | "Tất cả" | x | — | Giá trị mặc định: "Tất cả". Tất cả / 100% vốn nước ngoài / Liên doanh / Hợp đồng BCC / Khác. |
| 21 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 22 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

---

#### 2.4 Màn hình Chi tiết Dự án kêu gọi đầu tư (Tham chiếu: UC87 - Chi tiết dự án.png)

**Mô tả giao diện:**
Màn hình cuộn dọc hiển thị toàn bộ thông tin chi tiết của một dự án kêu gọi đầu tư, chia thành các section theo nhóm thông tin.

**Quy tắc chung hiển thị các Section:**
Các Section từ 1 đến 6 luôn luôn hiển thị trên giao diện; đối với các trường thông tin không có dữ liệu (null), hiển thị dấu gạch ngang "-" (áp dụng CMR-14). Riêng Section 7 (Tài liệu đính kèm) sẽ ẩn toàn bộ Section nếu không có tệp đính kèm nào.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về Danh sách (2.3). (CMR-06) |
| 2 | Tiêu đề Header | Label | "Chi tiết dự án" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng, giữa header. |

---

**Section 1 — Thông tin chung:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Mã dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu xanh dương. Null → `-` (CMR-14). |
| 4 | Tên dự án | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm (H1), hiển thị đầy đủ. |
| 5 | Loại dự án | Badge | — | — | — | **Quy tắc hiển thị:**<br>- "Trong nước" / "Nước ngoài" / "Trong & ngoài nước". |
| 6 | Lĩnh vực | Label | — | — | — | Null → `-` (CMR-14). |
| 7 | Ngành kinh tế | Label | — | — | — | Null → `-` (CMR-14). |
| 8 | Quốc gia triển khai dự án | Label | — | — | — | Null → `-` (CMR-14). |
| 9 | Địa bàn ưu đãi đầu tư | Label | — | — | — | Null → `-` (CMR-14). |
| 10 | Chính sách ưu đãi đầu tư | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 11 | Chính sách hỗ trợ đầu tư | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 12 | Hình thức đầu tư | Label | — | — | — | Null → `-` (CMR-14). |
| 13 | Link quảng bá dự án | Link (Tappable) | — | — | — | **Quy tắc hành động:**<br>- Tap → Mở trình duyệt mặc định. Null → Ẩn field (Exception CMR-14: field dạng Link/Tappable → ẩn khi null thay vì hiển thị "-"). |

---

**Section 2 — Cơ quan quản lý dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 14 | Tiêu đề section | Label | "Cơ quan quản lý dự án" | — | — | Font đậm, căn trái. |
| 15 | Tên đơn vị | Label | — | — | — | Null → `-` (CMR-14). |
| 16 | Địa chỉ | Label | — | — | — | Null → `-` (CMR-14). |
| 17 | Điện thoại | Label | — | — | — | Null → `-` (CMR-14). |
| 18 | Email | Label | — | — | — | Null → `-` (CMR-14). |

---

**Section 3 — Thông tin liên hệ tìm hiểu dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 19 | Tiêu đề section | Label | "Liên hệ tìm hiểu dự án" | — | — | Font đậm, căn trái. |
| 20 | Người liên hệ | Label | — | — | — | Null → `-` (CMR-14). |
| 21 | Chức vụ | Label | — | — | — | Null → `-` (CMR-14). |
| 22 | Điện thoại | Label | — | — | — | Null → `-` (CMR-14). |
| 23 | Email | Label | — | — | — | Null → `-` (CMR-14). |

---

**Section 4 — Mục tiêu & Quy mô dự án:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 24 | Tiêu đề section | Label | "Mục tiêu & Quy mô dự án" | — | — | Font đậm, căn trái. |
| 25 | Mục tiêu tổng quát | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 26 | Quy mô vốn thu hút đầu tư | Label | — | — | — | **Quy tắc hiển thị:**<br>- Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11). Null → `-` (CMR-14). |
| 27 | Diện tích đất sử dụng | Label | — | — | — | **Quy tắc hiển thị:**<br>- Đơn vị: ha hoặc m². Null → `-` (CMR-14). |
| 28 | Công nghệ sử dụng | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 29 | Sản phẩm/dịch vụ chính | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 30 | Nhu cầu lao động | Label | — | — | — | Null → `-` (CMR-14). |
| 31 | Nhu cầu về điện | Label | — | — | — | Null → `-` (CMR-14). |
| 32 | Nhu cầu về nước | Label | — | — | — | Null → `-` (CMR-14). |

---

**Section 5 — Nguồn vốn & Chi phí:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 33 | Tiêu đề section | Label | "Nguồn vốn & Chi phí" | — | — | Font đậm, căn trái. |
| 34 | Tổng vốn đầu tư dự kiến | Label | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đỏ. Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11). Null → `-` (CMR-14). |
| 35 | Ngân sách nhà nước | Label | — | — | — | Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11). Null → `-` (CMR-14). |
| 36 | Vốn nhà đầu tư | Label | — | — | — | CMR-11. Null → `-` (CMR-14). |
| 37 | Vốn vay | Label | — | — | — | CMR-11. Null → `-` (CMR-14). |
| 38 | Khác (tài trợ) | Label | — | — | — | CMR-11. Null → `-` (CMR-14). |
| 39 | Bảng hạng mục chi phí | Table (Scrollable) | — | — | — | **Quy tắc hiển thị:**<br>- Bảng cuộn ngang nếu vượt chiều rộng màn hình.<br>- Cột: Hạng mục chi phí đầu tư \| Nhóm chi phí \| NSNN \| Vốn vay \| Khác \| Tổng cộng.<br>- Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm (CMR-11).<br>- **Trạng thái Empty:** Nếu không có dữ liệu → "Không có dữ liệu." (CMR-14). |

---

**Section 6 — Tiến độ & Kế hoạch:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 40 | Tiêu đề section | Label | "Tiến độ & Kế hoạch" | — | — | Font đậm, căn trái. |
| 41 | Thời gian đầu tư | Label | — | — | — | Đơn vị: năm. Null → `-` (CMR-14). |
| 42 | Thời gian dự kiến bắt đầu hoạt động | Label | — | — | — | dd/MM/yyyy (CMR-12). Null → `-` (CMR-14). |
| 43 | Tiến độ dự kiến | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 44 | Kế hoạch chung | Label (Multiline) | — | — | — | Null → `-` (CMR-14). |
| 45 | Mong muốn tìm đối tác nước ngoài | Badge | — | — | — | **Quy tắc hiển thị:**<br>- "Có" (xanh lá) hoặc "Không" (xám). |
| 46 | Quốc gia mong muốn tìm đối tác | Label | — | — | — | Null → `-` (CMR-14). Chỉ hiển thị khi field #45 = "Có". |
| 47 | Bảng mốc kế hoạch triển khai | Table (Scrollable) | — | — | — | **Quy tắc hiển thị:**<br>- Cột: Giai đoạn \| Thời gian \| Mô tả.<br>- **Trạng thái Empty:** "Không có dữ liệu." (CMR-14). |

---

**Section 7 — Tài liệu đính kèm:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 48 | Tiêu đề section | Label | "Tài liệu đính kèm" | — | — | Font đậm, căn trái. |
| 49 | Danh sách tài liệu | List (File Item) | — | — | — | **Quy tắc hiển thị:**<br>- Mỗi item: Tên tài liệu + Loại tài liệu + Nút "Tải xuống".<br>- Tap nút "Tải xuống" → Xem/Tải theo CMR-08.<br>- **Trạng thái Empty:** Nếu không có tài liệu → Ẩn toàn bộ section. |

---

**Nút CTA cuối màn hình:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 50 | Nút "Đăng ký quan tâm" / "Hủy quan tâm" | Button (Primary/Secondary, Full-width) | — | — | — | **Quy tắc hiển thị:**<br>- Sticky bottom.<br>- Trạng thái mặc định: "Đăng ký quan tâm" (nền đỏ, text trắng).<br>- Nếu NĐT đã đăng ký: "Hủy quan tâm" (nền trắng, viền xám, text xám).<br>- **Loading state:** Khi đang chờ API → button disabled + hiển thị spinner cục bộ thay text (CMR-07). Sau khi API trả về → khôi phục trạng thái tương ứng.<br>**Quy tắc hành động:**<br>- Tap "Đăng ký quan tâm" → API đăng ký → Toast "Đăng ký quan tâm thành công." → Đổi trạng thái.<br>- Tap "Hủy quan tâm" → API hủy → Toast "Đã hủy đăng ký quan tâm." → Đổi lại trạng thái. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng bổ sung thông tin NĐT & Matching

1. NĐT vào Hub (2.1) → Tap "Bổ sung thông tin NĐT".
2. Hệ thống hiển thị form bổ sung (2.2). Nếu NĐT đã điền trước đó → form pre-fill dữ liệu cũ, cho phép sửa.
3. NĐT điền/sửa thông tin nhu cầu đầu tư → Nhấn "Xem dự án phù hợp".
4. Hệ thống gọi API matching (realtime). Loading toàn màn hình (CMR-07).
5. **Thuật toán matching (Hybrid):**
   - Form bắt buộc NĐT điền cả Lĩnh vực và Địa bàn. Khi matching, dự án chỉ cần khớp **ít nhất 1 trong 2 tiêu chí** (Lĩnh vực HOẶC Địa bàn) để được đưa vào kết quả.
   - Bonus: các tiêu chí còn lại (Ngành kinh tế, Hình thức đầu tư, Quy mô vốn, Quốc gia) tăng thứ tự ưu tiên.
   - Sắp xếp: mức độ phù hợp giảm dần (score không hiển thị cho NĐT).
6. API trả về kết quả → Điều hướng đến Màn hình 2.3 với danh sách matching mới (**thay thế hoàn toàn** danh sách cũ nếu có).
7. Nếu không có dự án phù hợp → Hiển thị "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng tra cứu danh sách dự án đề xuất

1. NĐT vào Hub (2.1) → Tap "Danh sách dự án đề xuất" → Màn hình 2.3.
2. Nếu NĐT **chưa từng bổ sung thông tin** → Hiển thị danh sách rỗng + thông báo "Vui lòng bổ sung thông tin để nhận gợi ý dự án phù hợp." + nút "Bổ sung ngay".
3. Nếu NĐT đã bổ sung → Hệ thống gọi API lấy danh sách dự án đề xuất (matching + gán thủ công).
4. Nguồn dữ liệu: Danh sách dự án kêu gọi NĐT trong nước + nước ngoài + trong & ngoài nước.
5. Sắp xếp mặc định: mức độ phù hợp giảm dần.
6. Infinite Scroll (CMR-04).
7. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.3 Luồng đăng ký / hủy đăng ký quan tâm dự án

1. NĐT tap "Đăng ký quan tâm" trên Card hoặc trong Chi tiết.
2. Hệ thống gọi API đăng ký quan tâm.
3. Tap nút "Đăng ký quan tâm" / "Hủy quan tâm" sẽ kích hoạt cơ chế loading trên button (disabled + spinner cục bộ theo CMR-07), đồng thời áp dụng cơ chế Debounce (CMR-18) chỉ nhận action đầu tiên cho đến khi có phản hồi API.
4. Thành công → Toast "Đăng ký quan tâm thành công." → Nút đổi thành "Hủy quan tâm".
5. NĐT tap "Hủy quan tâm" → Hệ thống gọi API hủy → Toast "Đã hủy đăng ký quan tâm." → Nút đổi lại "Đăng ký quan tâm".
6. Không giới hạn số dự án đăng ký quan tâm.
7. **Data sync:** Khi NĐT đăng ký/hủy quan tâm ở màn Chi tiết (§2.4) rồi quay lại Danh sách (§2.3), trạng thái nút trên Card tương ứng được cập nhật ngay (local state sync, không cần pull-to-refresh).
8. Thất bại → Hiển thị lỗi theo CMR-07.

#### 3.4 Xử lý lỗi (→ CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng / Mất kết nối | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + nút **"Thử lại"** | Giữ nguyên màn hình, hiển thị nút Thử lại. |
| Lỗi 401 (Session hết hạn) | *"Phiên đăng nhập hết hạn."* (Toast) | Auto refresh token. Nếu hết hạn >15 ngày → redirect Đăng nhập (CMR-07). |
| Lỗi API (HTTP 500) | *"Hệ thống đang bận. Vui lòng thử lại sau."* | Giữ nguyên màn hình. |
| Timeout (>10 giây) | *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + nút **"Thử lại"** | CMR-16. |

#### 3.5 Đa ngôn ngữ (→ CMR-17)

Toàn bộ text cứng (header, label, placeholder, thông báo lỗi, empty state) dịch 5 ngôn ngữ: VI, EN, ZH, JA, KO. Nội dung dữ liệu từ API hiển thị nguyên bản.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Hub hiển thị 2 khối chức năng chính (Bổ sung thông tin + Danh sách đề xuất), điều hướng đúng.
- **AC2:** Form bổ sung thông tin: pre-fill dữ liệu cũ khi quay lại, validate trường bắt buộc, matching realtime trả về kết quả.
- **AC3:** Matching Hybrid: kết quả phải khớp ít nhất 1 tiêu chí bắt buộc (Lĩnh vực HOẶC Địa bàn). Sắp xếp theo mức độ phù hợp giảm dần.
- **AC4:** Khi matching lại (sửa thông tin), danh sách cũ bị thay thế hoàn toàn.
- **AC5:** NĐT chưa bổ sung thông tin → vào Danh sách đề xuất → hiển thị empty state + nút "Bổ sung ngay".
- **AC6:** Đăng ký quan tâm: không giới hạn số lượng, nút đổi trạng thái đúng. Hủy đăng ký hoạt động chính xác.
- **AC7:** Chi tiết dự án hiển thị đầy đủ 7 section thông tin, null → `-`.
- **AC8:** Bảng hạng mục chi phí và bảng mốc kế hoạch cuộn ngang khi vượt chiều rộng.
- **AC9:** Tài liệu đính kèm tải/xem đúng (CMR-08).
- **AC10:** ~~NĐT nhận push notification khi có dự án mới được gán/matching.~~ → Chuyển sang UC Thông báo (UC riêng). UC87 không bao gồm luồng push notification.

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-11 | v1 → v1.2 | Tạo SRS ban đầu | (Không có) | SRS đơn giản: danh sách + tìm kiếm + lọc | File UC87_TraCuuDuAnKeuGoiDauTu.md |
| 2026-05-15 | v1.2 → v1.3 | Viết lại toàn bộ theo input chi tiết | Chỉ có màn hình danh sách đơn giản | Bổ sung: Hub 3 chức năng, Form matching NĐT, Danh sách đề xuất + Đăng ký quan tâm, Chi tiết dự án đầy đủ (7 section), NĐT tự đề xuất | Rewrite theo requirement mới |
| 2026-05-15 | v1.3 → v1.4 | §2.1, §2.2, §2.3, §2.4 — Tham chiếu wireframe | (Không có) | Bổ sung tham chiếu wireframe: UC87 - Onboard.png, UC87 - Bổ sung thông tin.png, UC87 - Dự án đề xuất.png, UC87 - Chưa có gợi ý.png, UC87 - Filter dự án.png, UC87 - Chi tiết dự án.png | Wireframe mới nhất |
| 2026-05-15 | v1.3 → v1.4 | §2.2 Tiêu đề Header | "Bổ sung thông tin NĐT" | "Bổ sung thông tin" | Khớp wireframe |
| 2026-05-15 | v1.4 → v1.5 | §1 Phân quyền | Chỉ ghi "Cá nhân / Tổ chức (Logged-in)" | Bổ sung: "Cá nhân và Tổ chức có cùng giao diện và chức năng, không phân biệt." | Audit Q1 |
| 2026-05-15 | v1.4 → v1.5 | §4 AC10 | "NĐT nhận push notification khi có dự án mới" | Chuyển sang UC Thông báo (UC riêng). UC87 không bao gồm push notification. | Audit Q2 |
| 2026-05-15 | v1.4 → v1.5 | §2.2 Multi-select | Không mô tả giới hạn và hiển thị | Không giới hạn số lượng, hiển thị dạng chip/tag, wrap xuống dòng | Audit Q4 |
| 2026-05-15 | v1.4 → v1.5 | §2.2 #7 Quy mô vốn | "Đơn vị: VNĐ hoặc USD (chọn bên cạnh)" | "Đơn vị: VNĐ (cố định)" — wireframe không có dropdown đơn vị | Audit Q5 |
| 2026-05-15 | v1.4 → v1.5 | §3.3 Data sync | (Không có) | Bổ sung: quay lại Danh sách từ Chi tiết → trạng thái nút cập nhật ngay (local state sync) | Audit Q6 |
| 2026-05-15 | v1.4 → v1.5 | §2.4 #13 Link null | "Null → Ẩn field" (không giải thích) | Bổ sung: "Exception CMR-14: field Link/Tappable → ẩn khi null" | Audit Q8 |
| 2026-05-15 | v1.4 → v1.5 | §3.1 step 5 Matching | "Bắt buộc: dự án phải khớp ít nhất 1 tiêu chí bắt buộc (Lĩnh vực HOẶC Địa bàn)" | Viết lại rõ: "Form bắt buộc điền cả 2. Matching chỉ cần khớp ít nhất 1 trong 2 để đưa vào kết quả." | Audit Q9 |
| 2026-05-15 | v1.4 → v1.5 | §2.2 Back dirty form | (Không có) | ~~CMR-10 đã bị xóa~~ | Audit Q10 |
| 2026-05-15 | v1.4 → v1.5 | §2.1 #3 Icon Chuông | "Badge đỏ khi có thông báo mới" | "Badge dạng dot đỏ (không hiển thị số)" + ref UC Thông báo riêng | Audit Q13 |
| 2026-05-18 | v1.5 → v1.6 | §2.3 #3 Ô tìm kiếm Placeholder | "Tìm kiếm dự án..." | "Tìm kiếm nhanh theo tên dự án, mã dự án" | CMR-01 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 #9 Textarea Placeholder | "Mô tả chi tiết nhu cầu đầu tư của bạn..." | "Nhập mô tả nhu cầu đầu tư" | CMR-09 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 #7 Textbox Placeholder | (Không có) | "Nhập quy mô vốn dự kiến" | CMR-09 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 #7, #9 Message lỗi Max length | (Không có) | Bổ sung: "[Tên trường] nhập quá ký tự cho phép" | CMR-09 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.2 Dropdown Placeholder | "Chọn lĩnh vực quan tâm...", "Chọn ngành kinh tế..." (có dấu ...) | Bỏ dấu "..." theo chuẩn: "Chọn [tên trường]" | CMR-03 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.3, §2.4 CMR-11 | Chỉ ghi ref "(CMR-11)" | Mô tả rõ: "Tự động phân tách hàng nghìn bằng dấu phẩy, thập phân bằng dấu chấm" | CMR-11 chuẩn MBFS |
| 2026-05-18 | v1.5 → v1.6 | §2.3 Filter Dropdown Placeholder | (Không có) | Bổ sung Placeholder: "Chọn [tên trường]" cho tất cả dropdown trong bộ lọc | CMR-03 chuẩn MBFS |
| 2026-05-19 | v1.6 → v1.7 | §2.3 #13, §2.4 #50 — Button loading state | (Không có) | Bổ sung: Khi đang chờ API → button disabled + spinner cục bộ thay text (CMR-07) | QC feedback Q1 |
| 2026-05-20 | v1.7 → v1.8 | §2.3 Tham chiếu wireframe Empty state | (Không có) | Bổ sung tham chiếu `UC87 - Dự án đề xuất - Empty state.png` vào header §2.3 | QC feedback |
| 2026-05-20 | v1.7 → v1.8 | §2.3 Trạng thái đặc biệt — Danh sách rỗng | (Không có) | Bổ sung: "Nếu matching không trả về kết quả hoặc tìm kiếm/lọc rỗng → hiển thị hình ảnh trống + 'Không có dữ liệu.' (CMR-14)" | QC feedback Q2 |
| 2026-05-20 | v1.7 → v1.8 | §2.4 Quy tắc chung hiển thị Section | (Không có) | Bổ sung: "Section 1-6 luôn hiển thị, field null → '-'. Section 7 ẩn toàn bộ khi không có file." | QC feedback Q2 |
| 2026-05-20 | v1.7 → v1.8 | §2.2 #7 Quy mô vốn — Validation > 0 | "Chỉ nhập số" | "Chỉ nhập số nguyên dương > 0 (không chấp nhận số âm, số 0 hay ký tự đặc biệt)" + message lỗi: "Quy mô vốn dự kiến phải lớn hơn 0" | QC feedback Q3 |
| 2026-05-20 | v1.7 → v1.8 | §1 Phân quyền — Role không hợp lệ | (Không có) | Bổ sung: "Token chứa role không hợp lệ → xử lý như lỗi 401 theo CMR-07" | QC feedback Q4 |
| 2026-05-20 | v1.7 → v1.8 | §1 Postconditions | "Hệ thống hiển thị danh sách dự án phù hợp hoặc cho phép NĐT đăng ký quan tâm dự án." | Tách rõ 3 postconditions: (a) sau bổ sung thông tin, (b) sau đăng ký quan tâm, (c) sau hủy quan tâm | QC feedback Q5 |
| 2026-05-20 | v1.7 → v1.8 | §3.3 step 3 — Loading + Debounce | "Hệ thống gọi API đăng ký quan tâm." (chỉ 1 dòng) | Bổ sung mô tả: loading trên button (disabled + spinner) + Debounce (CMR-18) chỉ nhận action đầu tiên | QC feedback Q1 (tích hợp vào luồng) |
| 2026-05-20 | v1.8 → v1.9 | §2.1 #3 — Badge thông báo | Badge dạng dot đỏ | Badge dạng dot vàng | QC feedback Q1 |
| 2026-05-20 | v1.8 → v1.9 | §2.1 #4, #5 — Nút action trên Card | Chỉ mô tả "Tap card → Điều hướng" | Bổ sung nút "Cập nhật" (Card 1) và "Xem danh sách" (Card 2) | QC feedback Q2 |
| 2026-05-20 | v1.8 → v1.9 | §2.2 #3 — Lĩnh vực quan tâm Searchable | Không có Searchable | Bổ sung Searchable (CMR-03) | QC feedback Q3/Q8 |
| 2026-05-20 | v1.8 → v1.9 | §2.2 Dropdown — Giá trị mặc định | Placeholder: "Chọn [tên trường]" | Giá trị mặc định: "Tất cả" cho tất cả dropdown (form + filter) | QC feedback Q4/Q6 |
| 2026-05-20 | v1.8 → v1.9 | §2.2 Multi-select — Chip/tag đồng nhất | Row 4, 8 chưa mô tả đầy đủ chip/tag | Bổ sung: "wrap xuống dòng khi hết chiều rộng. Mỗi chip có nút X để xóa." cho tất cả multi-select | QC feedback Q8 |
| 2026-05-20 | v1.8 → v1.9 | §2.3 Filter — Xóa Placeholder | Có Placeholder: "Chọn [tên trường]" | Xóa Placeholder, chỉ giữ giá trị mặc định "Tất cả" | QC feedback Q6 |
