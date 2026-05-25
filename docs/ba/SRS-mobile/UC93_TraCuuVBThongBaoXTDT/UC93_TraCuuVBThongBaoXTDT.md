# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC93 — Tra cứu văn bản thông báo tổ chức hoạt động XTĐT không sử dụng NSNN trên Mobile  
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

## UC93 — Tra cứu VB thông báo tổ chức hoạt động XTĐT không sử dụng NSNN

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu văn bản thông báo tổ chức hoạt động xúc tiến đầu tư không sử dụng ngân sách nhà nước
- **Mô tả:** Chức năng cho phép người dùng tra cứu, tìm kiếm và xem danh sách các văn bản thông báo về việc tổ chức hoạt động xúc tiến đầu tư sử dụng nguồn vốn ngoài ngân sách nhà nước (vốn tư nhân, vốn tài trợ quốc tế, v.v.).
- **Phân quyền:** Toàn bộ người dùng (Khách vãng lai và người dùng đã đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** KHÔNG bao gồm: tạo/gửi văn bản thông báo, phê duyệt văn bản, hoặc quản lý phía Admin.
- **Truy cập chức năng:** Sidebar → **"Xúc tiến đầu tư"** → **"VB thông báo XTĐT ngoài NSNN"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hiển thị danh sách văn bản hoặc trạng thái rỗng.
- **Chức năng đáp ứng usecase số:** UC93 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Văn bản thông báo

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về (CMR-06). |
| 2 | Tiêu đề Header | Label | "VB thông báo XTĐT" | — | — | Font đậm, màu trắng, giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Badge + Tap → Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm văn bản..." | x | — | Tối đa **255 ký tự** (CMR-01). Debounce 3s. Tìm theo Số hiệu VB, Tên tổ chức. Auto-trim. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Tap → Bottom Sheet (Năm, Tỉnh/TP, Loại hoạt động). Active filter indicator (CMR-02). |

**Danh sách Văn bản (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ văn bản (Card) | Container | — | — | — | Lazy load 20/lần (CMR-04). Pull to Refresh (CMR-13). |
| 7 | Số hiệu văn bản | Label | — | — | — | Font đậm, màu xanh dương. |
| 8 | Tên tổ chức thông báo | Label | — | — | — | Font đậm (H2). Tối đa 2 dòng, truncate. |
| 9 | Ngày ban hành | Icon + Label | — | — | — | Icon lịch + dd/MM/yyyy (CMR-12). |
| 10 | Loại hoạt động XTĐT | Icon + Label | — | — | — | Icon sự kiện + Tên loại (VD: "Hội nghị", "Triển lãm", "Roadshow"). |
| 11 | Địa điểm tổ chức | Icon + Label | — | — | — | Icon định vị + Tên địa điểm. |
| 12 | Nút Chi tiết | Button | "Chi tiết" | — | — | Tap → Chi tiết. Debounce (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Nút X (Đóng) | Button (Icon) | — | — | — | CMR-02. |
| 14 | Năm | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 15 | Tỉnh/Thành phố | Dropdown | "Tất cả" | x | — | Searchable (CMR-03). |
| 16 | Loại hoạt động | Dropdown | "Tất cả" | x | — | Hội nghị / Triển lãm / Roadshow / Hội thảo / Khác. |
| 17 | Nút "Áp dụng" | Button (Primary) | — | — | — | CMR-02. |
| 18 | Nút "Đặt lại" | Button (Secondary) | — | — | — | CMR-02. |

#### 2.3 Màn hình Chi tiết Văn bản thông báo

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về Danh sách (CMR-06). |
| 2 | Tiêu đề Header | Label | "Chi tiết văn bản" | — | — | Font đậm, màu trắng, giữa Header. |

**Khung Thông tin chi tiết:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 3 | Số hiệu văn bản | Label | — | — | — | Font đậm, màu xanh dương. |
| 4 | Tên tổ chức thông báo | Label | — | — | — | Font đậm (H1). |
| 5 | Ngày ban hành | Label | — | — | — | dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 6 | Loại hoạt động XTĐT | Label | — | — | — | Null → "-" (CMR-14). |
| 7 | Tên hoạt động | Label | — | — | — | Tên cụ thể của sự kiện/hoạt động. Null → "-" (CMR-14). |
| 8 | Thời gian tổ chức | Label | — | — | — | dd/MM/yyyy - dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 9 | Địa điểm tổ chức | Label | — | — | — | Null → "-" (CMR-14). |
| 10 | Nguồn vốn | Label | — | — | — | Mô tả nguồn vốn (VD: "Vốn tư nhân", "Tài trợ quốc tế"). Null → "-" (CMR-14). |
| 11 | Nội dung hoạt động | Label (Multiline) | — | — | — | Mô tả chi tiết. Null → "-" (CMR-14). |
| 12 | Đối tượng tham gia | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 13 | Tài liệu đính kèm | File List | — | — | — | CMR-08. Không có → Ẩn section. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách
1. API lấy danh sách VB thông báo XTĐT không sử dụng NSNN.
2. Sắp xếp: ngày ban hành mới nhất lên đầu.
3. Infinite Scroll (CMR-04).
4. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Realtime theo số hiệu VB + tên tổ chức. Debounce 3s (CMR-01). Không tìm thấy → "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** API kèm (Year, ProvinceID, ActivityType).
3. **Kết hợp:** Tìm kiếm + Lọc đồng thời (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Tap "Chi tiết" → API chi tiết văn bản.
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

- **AC1:** Card hiển thị: Số hiệu, Tên tổ chức, Ngày ban hành, Loại hoạt động, Địa điểm.
- **AC2:** Bộ lọc 3 tiêu chí (Năm, Tỉnh/TP, Loại hoạt động).
- **AC3:** Tìm kiếm theo số hiệu + tên tổ chức, debounce 3s.
- **AC4:** Chi tiết hiển thị đầy đủ, null → "-".
- **AC5:** Tài liệu đính kèm (CMR-08).

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC93 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |
