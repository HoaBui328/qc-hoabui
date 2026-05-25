# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC91 — Tra cứu văn bản thỏa thuận hợp tác MOU trên Mobile  
**Ngày tạo:** 14/05/2026  
**Tác giả:** Agent 6 (Mobile FDD Architect)  
**Phiên bản:** v1

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | han.luong & huy.lai2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Khai thác thông tin xúc tiến đầu tư |
| Đối tượng thực hiện | Cá nhân / Tổ chức (Guest & Logged-in) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 14/05/2026 |
| Phiên bản | v1 |

---

## UC91 — Tra cứu văn bản thỏa thuận hợp tác MOU trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu văn bản thỏa thuận hợp tác (MOU)
- **Mô tả:** Chức năng cho phép người dùng tra cứu, tìm kiếm và xem danh sách các văn bản Thỏa thuận hợp tác (Memorandum of Understanding - MOU) giữa Việt Nam và các đối tác quốc tế trong lĩnh vực đầu tư.
- **Phân quyền:** Toàn bộ người dùng (Khách vãng lai và người dùng đã đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** KHÔNG bao gồm: ký kết MOU mới, chỉnh sửa MOU, hoặc quản lý MOU phía Admin.
- **Truy cập chức năng:** Sidebar → **"Xúc tiến đầu tư"** → **"Văn bản MOU"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hiển thị danh sách MOU hoặc trạng thái rỗng.
- **Chức năng đáp ứng usecase số:** UC91 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Văn bản MOU

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về (CMR-06). |
| 2 | Tiêu đề Header | Label | "Văn bản MOU" | — | — | Font đậm, màu trắng, giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Badge + Tap → Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm văn bản MOU..." | x | — | Tối đa **255 ký tự** (CMR-01). Debounce 3s. Tìm theo Tên văn bản, Đối tác ký kết. Auto-trim. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Tap → Bottom Sheet (Quốc gia đối tác, Năm ký kết, Lĩnh vực, Trạng thái). Active filter indicator (CMR-02). |

**Danh sách MOU (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ MOU (Card) | Container | — | — | — | Lazy load 20/lần (CMR-04). Pull to Refresh (CMR-13). |
| 7 | Tên văn bản MOU | Label | — | — | — | Font đậm, tối đa 2 dòng, truncate. |
| 8 | Đối tác ký kết | Icon + Label | — | — | — | Icon bắt tay + Tên đối tác/quốc gia (VD: "Nhật Bản", "Hàn Quốc - Samsung"). |
| 9 | Ngày ký kết | Icon + Label | — | — | — | Icon lịch + dd/MM/yyyy (CMR-12). |
| 10 | Lĩnh vực hợp tác | Icon + Label | — | — | — | Icon ngành + Tên lĩnh vực. |
| 11 | Trạng thái | Badge | — | — | — | CMR-05: Xanh lá = "Còn hiệu lực", Đỏ = "Hết hiệu lực", Vàng = "Chờ ký kết". |
| 12 | Nút Chi tiết | Button | "Chi tiết" | — | — | Tap → Chi tiết MOU. Debounce (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Nút X (Đóng) | Button (Icon) | — | — | — | CMR-02. |
| 14 | Quốc gia đối tác | Dropdown | "Tất cả" | x | — | Danh sách quốc gia từ API. Searchable (CMR-03). |
| 15 | Năm ký kết | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 16 | Lĩnh vực hợp tác | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 17 | Trạng thái | Dropdown | "Tất cả" | x | — | Tất cả / Còn hiệu lực / Hết hiệu lực / Chờ ký kết. |
| 18 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 19 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

#### 2.3 Màn hình Chi tiết Văn bản MOU

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về Danh sách (CMR-06). |
| 2 | Tiêu đề Header | Label | "Chi tiết văn bản MOU" | — | — | Font đậm, màu trắng, giữa Header. |

**Khung Thông tin chi tiết:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Tên văn bản MOU | Label | — | — | — | Font đậm (H1), hiển thị đầy đủ. |
| 4 | Trạng thái | Badge | — | — | — | CMR-05. |
| 5 | Số hiệu văn bản | Label | — | — | — | Null → "-" (CMR-14). |
| 6 | Đối tác ký kết | Label | — | — | — | Tên tổ chức/quốc gia đối tác. Null → "-" (CMR-14). |
| 7 | Bên Việt Nam ký kết | Label | — | — | — | Tên cơ quan/tổ chức phía VN. Null → "-" (CMR-14). |
| 8 | Ngày ký kết | Label | — | — | — | dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 9 | Ngày hết hiệu lực | Label | — | — | — | dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 10 | Lĩnh vực hợp tác | Label | — | — | — | Null → "-" (CMR-14). |
| 11 | Nội dung tóm tắt | Label (Multiline) | — | — | — | Mô tả nội dung chính của MOU. Null → "-" (CMR-14). |
| 12 | Phạm vi áp dụng | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 13 | Địa điểm ký kết | Label | — | — | — | Null → "-" (CMR-14). |
| 14 | Tài liệu đính kèm | File List | — | — | — | CMR-08. Không có → Ẩn section. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách
1. API lấy danh sách văn bản MOU.
2. Sắp xếp: ngày ký kết mới nhất lên đầu.
3. Infinite Scroll (CMR-04).
4. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Realtime theo tên văn bản + đối tác ký kết. Debounce 3s (CMR-01). Không tìm thấy → "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** API kèm (CountryID, Year, IndustryID, Status).
3. **Kết hợp:** Tìm kiếm + Lọc đồng thời (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Tap "Chi tiết" → API chi tiết MOU.
2. Loading toàn màn hình (CMR-07).
3. Null → "-" (CMR-14).

#### 3.4 Xử lý lỗi (CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng | "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + "Thử lại" | Giữ nguyên. |
| Lỗi 401 | "Phiên đăng nhập hết hạn." (Toast) | Auto refresh → redirect nếu hết hạn (CMR-07). |
| Lỗi 500 | "Hệ thống đang bận. Vui lòng thử lại sau." | Giữ nguyên. |
| Timeout (>10s) | "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + "Thử lại" | CMR-16. |

#### 3.5 Đa ngôn ngữ (CMR-17)

Text cứng dịch 5 ngôn ngữ. Nội dung API giữ nguyên bản.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Card hiển thị: Tên MOU, Đối tác, Ngày ký, Lĩnh vực, Trạng thái.
- **AC2:** Bộ lọc 4 tiêu chí (Quốc gia, Năm, Lĩnh vực, Trạng thái).
- **AC3:** Tìm kiếm theo tên + đối tác, debounce 3s.
- **AC4:** Chi tiết hiển thị đầy đủ thông tin MOU, null → "-".
- **AC5:** Tài liệu đính kèm mở/tải đúng (CMR-08).
- **AC6:** MOU hết hiệu lực hiển thị badge đỏ rõ ràng.

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC91 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |
