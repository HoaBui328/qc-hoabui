# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC90 — Tra cứu chương trình xúc tiến đầu tư Địa phương trên Mobile  
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

## UC90 — Tra cứu chương trình xúc tiến đầu tư Địa phương trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu chương trình xúc tiến đầu tư Địa phương
- **Mô tả:** Chức năng cho phép người dùng tra cứu, tìm kiếm và xem danh sách các chương trình xúc tiến đầu tư do các Tỉnh/Thành phố trực thuộc Trung ương chủ trì.
- **Phân quyền:** Toàn bộ người dùng (Khách vãng lai và người dùng đã đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** KHÔNG bao gồm: CT XTĐT Quốc gia (UC88), CT XTĐT Bộ ngành (UC89).
- **Truy cập chức năng:** Sidebar → **"Xúc tiến đầu tư"** → **"CT XTĐT Địa phương"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hiển thị danh sách chương trình hoặc trạng thái rỗng.
- **Chức năng đáp ứng usecase số:** UC90 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Chương trình XTĐT Địa phương

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về màn hình trước (CMR-06). |
| 2 | Tiêu đề Header | Label | "CT XTĐT Địa phương" | — | — | Font đậm, màu trắng, giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Badge + Tap → Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm nhanh theo tên chương trình" | x | — | Tối đa **255 ký tự** (CMR-01). Debounce 3s. Tìm theo Tên CT. Auto-trim whitespace. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Tap → Bottom Sheet (Năm, Tỉnh/TP, Lĩnh vực, Trạng thái). Active filter indicator (CMR-02). |

**Danh sách Chương trình (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ chương trình (Card) | Container | — | — | — | Lazy load 20/lần (CMR-04). Pull to Refresh (CMR-13). |
| 7 | Tên chương trình | Label | — | — | — | Font đậm, tối đa 2 dòng, truncate. |
| 8 | Năm thực hiện | Icon + Label | — | — | — | Icon lịch + Năm. |
| 9 | Tỉnh/Thành phố | Icon + Label | — | — | — | Icon định vị + Tên tỉnh/TP (VD: "Hà Nội", "TP. Hồ Chí Minh"). |
| 10 | Lĩnh vực | Icon + Label | — | — | — | Icon ngành + Tên lĩnh vực. |
| 11 | Trạng thái | Badge | — | — | — | CMR-05. |
| 12 | Nút Chi tiết | Button | "Chi tiết" | — | — | Tap → Chi tiết. Debounce (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Nút X (Đóng) | Button (Icon) | — | — | — | Đóng, không thay đổi kết quả (CMR-02). |
| 14 | Năm | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 15 | Tỉnh/Thành phố | Dropdown | "Tất cả" | x | — | Danh sách 63 tỉnh/TP từ API. Searchable (CMR-03). |
| 16 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 17 | Trạng thái | Dropdown | "Tất cả" | x | — | Tất cả / Đang thực hiện / Chưa triển khai / Đã kết thúc. |
| 18 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 19 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

#### 2.3 Màn hình Chi tiết Chương trình XTĐT Địa phương

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về Danh sách (CMR-06). |
| 2 | Tiêu đề Header | Label | "Chi tiết chương trình" | — | — | Font đậm, màu trắng, giữa Header. |

**Khung Thông tin chi tiết:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Tên chương trình | Label | — | — | — | Font đậm (H1), hiển thị đầy đủ. |
| 4 | Trạng thái | Badge | — | — | — | CMR-05. |
| 5 | Năm thực hiện | Label | — | — | — | "Năm [YYYY]". |
| 6 | Tỉnh/Thành phố chủ trì | Label | — | — | — | Null → "-" (CMR-14). |
| 7 | Lĩnh vực đầu tư | Label | — | — | — | Null → "-" (CMR-14). |
| 8 | Mục tiêu chương trình | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 9 | Nội dung hoạt động | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 10 | Kinh phí dự kiến | Label | — | — | — | CMR-11. Null → "-" (CMR-14). |
| 11 | Thời gian thực hiện | Label | — | — | — | dd/MM/yyyy - dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 12 | Địa điểm thực hiện | Label | — | — | — | Null → "-" (CMR-14). |
| 13 | Tài liệu đính kèm | File List | — | — | — | CMR-08. Không có → Ẩn section. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách
1. API lấy danh sách CT XTĐT Địa phương.
2. Sắp xếp: năm mới nhất → ngày tạo mới nhất.
3. Infinite Scroll (CMR-04).
4. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Realtime theo tên CT. Debounce 3s (CMR-01). Không tìm thấy → "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** API kèm (Year, ProvinceID, IndustryID, Status).
3. **Kết hợp:** Tìm kiếm + Lọc đồng thời (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Tap "Chi tiết" → API chi tiết.
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

- **AC1:** Card hiển thị: Tên, Năm, Tỉnh/TP, Lĩnh vực, Trạng thái.
- **AC2:** Bộ lọc 4 tiêu chí (Năm, Tỉnh/TP, Lĩnh vực, Trạng thái) hoạt động chính xác.
- **AC3:** Tìm kiếm debounce + kết hợp bộ lọc.
- **AC4:** Chi tiết hiển thị đầy đủ, null → "-".
- **AC5:** Tài liệu đính kèm (CMR-08).

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC90 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |
