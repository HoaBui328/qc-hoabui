# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC89 — Tra cứu chương trình xúc tiến đầu tư Bộ ngành trên Mobile  
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

## UC89 — Tra cứu chương trình xúc tiến đầu tư Bộ ngành trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu chương trình xúc tiến đầu tư Bộ ngành
- **Mô tả:** Chức năng cho phép người dùng tra cứu, tìm kiếm và xem danh sách các chương trình xúc tiến đầu tư do các Bộ, ngành chủ trì theo nhiều tiêu chí.
- **Phân quyền:** Toàn bộ người dùng (Khách vãng lai và người dùng đã đăng nhập).
- **Phạm vi ngoài UC (Exclusions):** UC này KHÔNG bao gồm: tra cứu CT XTĐT Quốc gia (UC88), tra cứu CT XTĐT Địa phương (UC90).
- **Truy cập chức năng:** Sidebar → Mục **"Xúc tiến đầu tư"** → Chọn **"CT XTĐT Bộ ngành"**.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định (Wifi/4G/5G).
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị danh sách các chương trình XTĐT Bộ ngành thỏa mãn điều kiện hoặc hiển thị trạng thái rỗng.
- **Chức năng đáp ứng usecase số:** UC89 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Chương trình XTĐT Bộ ngành

**Mô tả giao diện:**
Màn hình danh sách với Header đỏ đậm. Thanh công cụ gồm Ô tìm kiếm và Nút lọc. Phần thân hiển thị danh sách Card cuộn dọc.

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | Tap → Quay về màn hình trước đó (CMR-06). |
| 2 | Tiêu đề Header | Label | "CT XTĐT Bộ ngành" | — | — | Font đậm, màu trắng, nằm giữa Header. |
| 3 | Icon Thông báo (Chuông) | Button (Icon) | — | — | — | Icon chuông trắng + Badge. Tap → Trung tâm thông báo. |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm nhanh theo tên chương trình" | x | — | Tối đa **255 ký tự** (CMR-01). Debounce 3 giây. Tìm theo Tên chương trình. Auto-trim whitespace. |
| 5 | Nút Lọc | Button (Icon) | — | — | — | Tap → Mở Bottom Sheet bộ lọc (Năm, Bộ ngành, Lĩnh vực, Trạng thái). Active filter indicator (CMR-02). |

**Danh sách Chương trình (List Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Thẻ chương trình (Card) | Container | — | — | — | Khung trắng, bo góc, shadow nhẹ. Lazy load 20 bản ghi/lần (CMR-04). Pull to Refresh (CMR-13). |
| 7 | Tên chương trình | Label | — | — | — | Font đậm (H2), màu đen. Tối đa 2 dòng, truncate `...`. |
| 8 | Năm thực hiện | Icon + Label | — | — | — | Icon lịch + Năm. |
| 9 | Bộ ngành chủ trì | Icon + Label | — | — | — | Icon tòa nhà + Tên Bộ/ngành (VD: "Bộ Công Thương", "Bộ Nông nghiệp và PTNT"). |
| 10 | Lĩnh vực | Icon + Label | — | — | — | Icon ngành + Tên lĩnh vực. |
| 11 | Trạng thái | Badge | — | — | — | CMR-05: Xanh lá = "Đang thực hiện", Vàng = "Chưa triển khai", Xám = "Đã kết thúc". |
| 12 | Nút Chi tiết | Button | "Chi tiết" | — | — | Tap → Màn hình Chi tiết. Debounce Navigation (CMR-18). |

#### 2.2 Modal Bottom Sheet — Bộ lọc

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Nút X (Đóng) | Button (Icon) | — | — | — | Đóng Bottom Sheet, không thay đổi kết quả (CMR-02). |
| 14 | Năm | Dropdown | "Tất cả" | x | — | Danh sách năm từ API. Searchable (CMR-03). |
| 15 | Bộ ngành | Dropdown | "Tất cả" | x | — | Danh sách Bộ/ngành từ API. Searchable (CMR-03). |
| 16 | Lĩnh vực | Dropdown | "Tất cả" | x | — | Danh sách lĩnh vực từ API. Searchable (CMR-03). |
| 17 | Trạng thái | Dropdown | "Tất cả" | x | — | Tất cả / Đang thực hiện / Chưa triển khai / Đã kết thúc. |
| 18 | Nút "Áp dụng" | Button (Primary) | — | — | — | Đóng bộ lọc, tải lại danh sách (CMR-02). |
| 19 | Nút "Đặt lại" | Button (Secondary) | — | — | — | Reset về mặc định (CMR-02). |

#### 2.3 Màn hình Chi tiết Chương trình XTĐT Bộ ngành

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
| 6 | Bộ ngành chủ trì | Label | — | — | — | Tên Bộ/ngành. Null → "-" (CMR-14). |
| 7 | Lĩnh vực đầu tư | Label | — | — | — | Null → "-" (CMR-14). |
| 8 | Mục tiêu chương trình | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 9 | Nội dung hoạt động | Label (Multiline) | — | — | — | Null → "-" (CMR-14). |
| 10 | Kinh phí dự kiến | Label | — | — | — | Định dạng CMR-11. Null → "-" (CMR-14). |
| 11 | Thời gian thực hiện | Label | — | — | — | dd/MM/yyyy - dd/MM/yyyy (CMR-12). Null → "-" (CMR-14). |
| 12 | Địa điểm thực hiện | Label | — | — | — | Null → "-" (CMR-14). |
| 13 | Tài liệu đính kèm | File List | — | — | — | Tap → Xem/Tải (CMR-08). Không có file → Ẩn section. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng tải danh sách
1. Hệ thống gọi API lấy danh sách chương trình XTĐT Bộ ngành.
2. Mặc định sắp xếp theo năm mới nhất, trong cùng năm theo ngày tạo mới nhất.
3. Infinite Scroll theo CMR-04.
4. Không có dữ liệu → "Không có dữ liệu." (CMR-14).

#### 3.2 Luồng Tìm kiếm & Lọc
1. **Tìm kiếm:** Realtime theo tên chương trình. Debounce 3 giây (CMR-01). Không tìm thấy → "Không tìm thấy dữ liệu" (CMR-14).
2. **Lọc:** API kèm tham số (Year, MinistryID, IndustryID, Status).
3. **Kết hợp:** Tìm kiếm + Lọc đồng thời (CMR-01).

#### 3.3 Luồng xem chi tiết
1. Tap "Chi tiết" → API lấy chi tiết chương trình.
2. Loading state toàn màn hình (CMR-07).
3. Hiển thị thông tin. Null → "-" (CMR-14).

#### 3.4 Xử lý lỗi (CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
|---|---|---|
| Lỗi mạng | "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + "Thử lại" | Giữ nguyên màn hình. |
| Lỗi 401 | "Phiên đăng nhập hết hạn." (Toast) | Auto refresh token → redirect Đăng nhập nếu hết hạn (CMR-07). |
| Lỗi 500 | "Hệ thống đang bận. Vui lòng thử lại sau." | Giữ nguyên màn hình. |
| Timeout (>10s) | "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + "Thử lại" | CMR-16. |

#### 3.5 Đa ngôn ngữ (CMR-17)

Text cứng dịch 5 ngôn ngữ (VI, EN, ZH, JA, KO). Nội dung API giữ nguyên bản.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Card hiển thị đầy đủ: Tên, Năm, Bộ ngành chủ trì, Lĩnh vực, Trạng thái.
- **AC2:** Bộ lọc hoạt động với 4 tiêu chí (Năm, Bộ ngành, Lĩnh vực, Trạng thái).
- **AC3:** Tìm kiếm debounce 3 giây, kết hợp bộ lọc chính xác.
- **AC4:** Chi tiết hiển thị đầy đủ, null → "-".
- **AC5:** Tài liệu đính kèm mở/tải đúng (CMR-08).

---

### 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
|---|---|---|---|---|---|
| 2026-05-14 | v1 | Khởi tạo | (Không có) | Tạo mới SRS UC89 | Assume từ Phụ lục XIV + CMR Mobile |
| 2026-05-21 | v1 → v1.1 | Align CMR v6.1 | Ô tìm kiếm max 500 ký tự | Ô tìm kiếm max **255 ký tự** (CMR-01) | Đồng bộ CMR Mobile 20260520 |
