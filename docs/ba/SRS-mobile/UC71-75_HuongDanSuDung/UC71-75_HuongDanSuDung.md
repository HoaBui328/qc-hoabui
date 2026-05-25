# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC71-75 — Hướng dẫn sử dụng trên Mobile
**Ngày tạo:** 16/05/2026

| Thuộc tính   | Giá trị                    |
| -------------- | ---------------------------- |
| Mã Use Case   | UC71, UC72, UC73, UC74, UC75 |
| Tên Use Case  | Hướng dẫn sử dụng       |
| BA phụ trách | huy.lai2                     |
| Giao diện     | Màn hình Mobile (Portrait) |
| Ngày tạo     | 16/05/2026                   |
| Phiên bản    | v1.8                         |

---

### 1. Mô tả chức năng

**Tên chức năng:** Hướng dẫn sử dụng trên Mobile
**Mô tả:** Nhóm chức năng hỗ trợ người dùng tra cứu hướng dẫn sử dụng ứng dụng. Phần Hướng dẫn hiển thị danh mục dạng **Grid Cards** (chọn card → xem chi tiết các bước thực hiện dạng numbered steps). Giúp người dùng tự giải quyết vướng mắc mà không cần liên hệ hỗ trợ.
**Phân quyền:** Cá nhân/Tổ chức (không yêu cầu đăng nhập — public access).
**Truy cập chức năng:** Sidebar → "Hướng dẫn sử dụng". Hoặc: Footer (Bottom Navigation) → Tab **"Hướng dẫn sử dụng"**.
**Phạm vi ngoài UC (Exclusions):** UC71-75 KHÔNG bao gồm: chỉnh sửa/quản lý nội dung hướng dẫn (thuộc CMS Admin), icon chuông thông báo (không có trên các màn hình UC71-75).
**Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
**Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị đầy đủ nội dung hướng dẫn trên màn hình.
**Accessibility:** Touch target tối thiểu 44x44dp (theo platform guideline). Contrast ratio tuân theo WCAG 2.1 AA.
**Compatibility:** iOS 15+, Android 8.0+. Chỉ hỗ trợ Portrait.
**Chức năng đáp ứng usecase số:**

- UC71: Tra cứu hướng dẫn sử dụng về đăng nhập, đăng ký tài khoản trên mobile
- UC72: Tra cứu hướng dẫn sử dụng về dịch vụ công trực tuyến trên mobile
- UC73: Tra cứu hướng dẫn sử dụng về tra cứu văn bản pháp luật, thủ tục hành chính trên mobile
- UC74: Tra cứu hướng dẫn sử dụng về kết nối đối tác trên mobile
- UC75: Tra cứu hướng dẫn sử dụng trên mobile

---

### 2. Giao diện người dùng (Mô tả chi tiết component)

#### 2.1 Màn hình Hub Hướng dẫn sử dụng

**Mô tả giao diện:**
Màn hình hiển thị danh mục hướng dẫn dạng **Grid Cards** (lưới 2 cột). Mỗi Card bao gồm: Icon minh họa, tiêu đề, mô tả ngắn và nút "Xem hướng dẫn >" (text màu đỏ). Nội dung chỉ đọc (read-only), người dùng tap nút "Xem hướng dẫn >" để điều hướng sang màn hình chi tiết tương ứng.

| # | Tên trường        | Kiểu trường     | Giá trị mặc định    | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------- | ------------------ | ------------------------ | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nút Quay lại (←)  | Button (Icon)      | —                       | —           | —         | **Quy tắc hành động:**`<br>`- Tap → Quay về màn hình trước (Sidebar hoặc màn hình gọi). (Xem CMR-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2 | Tiêu đề Header    | Label              | "Hướng dẫn sử dụng" | —           | —         | **Quy tắc hiển thị:**`<br>`- Nằm giữa header, màu trắng trên nền đỏ đậm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 3 | Banner giới thiệu  | Banner (Dark Red)  | —                       | —           | —         | **Quy tắc hiển thị:**`<br>`- Nền đỏ đậm, nằm ngay dưới header.`<br>`- Text: *"Tài liệu hướng dẫn chi tiết giúp bạn tận dụng tối đa các tính năng của hệ thống"* (màu trắng).`<br>`- Nội dung **static** (hard-coded), không lấy từ API.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 4 | Section label        | Label              | "Danh mục hướng dẫn" | —           | —         | **Quy tắc hiển thị:**`<br>`- Font đậm, căn trái, nằm phía trên Grid Cards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 5 | Grid Cards danh mục | Card Grid (2 cột) | —                       | —           | —         | **Quy tắc hiển thị:**`<br>`- Lưới 2 cột, mỗi Card gồm: Icon minh hoạ (nền xám nhạt, bo tròn) + Tiêu đề (font đậm) + Mô tả ngắn (font thường) + Button "Xem hướng dẫn >" (text đỏ).`<br>`- Nền trắng, bo góc, shadow nhẹ.`<br>`- Danh sách Cards được **Admin config từ Admin Site** (dynamic từ API, không hard-code). Sắp xếp theo tên danh mục 0-9/A-Z.`<br>`- Nếu tên danh mục quá dài → truncate với ellipsis (...).`<br>`- **Empty state:** Nếu danh sách từ API trả về rỗng (Admin chưa cấu hình), hiển thị thông báo *"Không có dữ liệu"* (theo chuẩn CMR-14).`<br><br>`**Quy tắc hành động:**`<br>`- Tap "Xem hướng dẫn >" → Điều hướng sang màn hình chi tiết tương ứng.`<br>`- **Debounce Navigation (CMR-18):** Tap nhanh liên tục → chỉ nhận action đầu tiên, bỏ qua các tap tiếp theo cho đến khi điều hướng hoàn tất. |

---

#### 2.2 Màn hình Chi tiết Hướng dẫn sử dụng

**Mô tả giao diện:**
Màn hình hiển thị toàn bộ nội dung hướng dẫn của một danh mục. Header hiển thị **tên danh mục hướng dẫn** (dynamic từ Admin Site). Vùng nội dung hiển thị đầy đủ text hướng dẫn theo cấu hình từ Admin Site — chỉ đọc (read-only), cuộn dọc. Nếu nội dung dài → tự động wrap text, không truncate.

| # | Tên trường                      | Kiểu trường | Giá trị mặc định                                 | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------- | -------------- | ----------------------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nút Quay lại (←)                | Button (Icon)  | —                                                    | —           | —         | **Quy tắc hành động:**`<br>`- Tap → Quay về màn hình Hub UC75. (Xem CMR-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2 | Tiêu đề Header (Tên danh mục) | Label (Sticky) | Dynamic — lấy từ tên danh mục hướng dẫn (API) | —           | —         | **Quy tắc hiển thị:**`<br>`- Hiển thị **tên danh mục hướng dẫn** tương ứng với Card đã chọn ở màn Hub (ví dụ: "Đăng nhập tài khoản", "Dịch vụ công trực tuyến").`<br>`- Nằm giữa header, màu trắng trên nền đỏ đậm.`<br>`- Nội dung **dynamic** — lấy từ API/Admin Site, không hard-code.`<br>`- Nếu tên danh mục quá dài → **wrap text**. |
| 3 | Nội dung hướng dẫn             | Rich Text      | —                                                    | —           | —         | **Quy tắc hiển thị:**`<br>`- Hiển thị **đầy đủ** nội dung hướng dẫn theo config từ Admin Site — không truncate, không giới hạn số dòng.`<br>`- Nếu nội dung dài → **wrap text** tự động (không tràn ra ngoài màn hình).`<br>`- Hỗ trợ **Rich Text** (bold, italic, ...) theo configuration từ Admin Site.`<br>`- Nội dung **dynamic** — lấy từ API/Admin Site.`<br>`- **Empty state:** Nếu nội dung null hoặc rỗng → hiển thị *"Không có dữ liệu"* (CMR-14).`<br>`- **Cuộn dọc:** Toàn bộ màn hình cuộn dọc để xem hết nội dung khi nội dung dài hơn viewport. |

> **Lưu ý thiết kế:** Màn hình chi tiết **không có Tab Bar, không có Numbered Steps, không có Banner giới thiệu** — chỉ có header (tên danh mục dynamic) + vùng nội dung Rich Text. Toàn bộ nội dung luôn hiển thị đầy đủ, không cần nút "Xem thêm" hay expand/collapse.

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý xem hướng dẫn

1. Người dùng tap vào nút "Xem hướng dẫn >" tại màn hình Hub.
   - **Debounce Navigation (CMR-18):** Khi người dùng tap nhanh liên tục (double tap) vào button "Xem hướng dẫn >", hệ thống chỉ nhận action đầu tiên và bỏ qua các tap tiếp theo cho đến khi điều hướng hoàn tất.
2. Hệ thống tải dữ liệu các bước thực hiện từ CMS.
   - **Loading state (CMR-07):** Trong khi chờ API phản hồi, hiển thị **loading indicator** (spinner). Ẩn loading indicator khi dữ liệu đã tải xong.
   - **Quy định thời gian phản hồi:** Tối đa 10 giây cho API. Quá 10 giây → Hiển thị "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." kèm nút "Thử lại".
3. Nội dung hướng dẫn hiển thị dạng **text label** — chỉ đọc (read-only). Nếu nội dung dài → **wrap text** tự động. Toàn bộ nội dung hiển thị đầy đủ trên 1 màn hình cuộn dọc, không truncate.
4. **Pull to Refresh (CMR-13):** Kéo xuống từ đầu nội dung để tải lại dữ liệu từ CMS/API.
5. **Nút Back (Android hardware):** Khi nhấn nút Back vật lý trên Android → Quay về màn hình Hub UC75 (cùng hành vi với nút ← trên header).

#### 3.2 Xử lý lỗi (→ Xem CMR-07)

| Quy tắc       | Mô tả                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lỗi mạng     | Hiển thị thông báo: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* Kèm nút "Thử lại". Tap "Thử lại" → nút chuyển sang **loading state (disabled)** trong khi gọi API → enabled lại sau khi API trả về (CMR I08).                                        |
| Lỗi API (500) | Hiển thị thông báo: *"Hệ thống đang bận. Vui lòng thử lại sau."*                                                                               |
| Lỗi 404       | Hiển thị: *"Nội dung không tồn tại hoặc đã bị xóa."*                                                                                           |
| Lỗi 401 (Session hết hạn) | Hệ thống sẽ tự động sử dụng **refresh token** để cấp lại access token mới. Nếu refresh token đã hết hạn hoặc không hợp lệ (quá **15 ngày**), người dùng sẽ được chuyển về **màn hình đăng nhập** và hiển thị **toast**: *"Phiên đăng nhập hết hạn."* |
| Timeout        | Nếu API không phản hồi trong **10 giây** → Hiển thị thông báo: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* Kèm nút "Thử lại". Tap "Thử lại" → nút chuyển sang **loading state (disabled)** trong khi gọi API → enabled lại sau khi API trả về (CMR I08). |
| Loading state  | Mọi API call phải có loading indicator trong khi chờ kết quả. Đối với **first-load** màn hình danh sách hoặc chi tiết, sử dụng **loading state toàn màn hình** (full-screen loading overlay). Các lần tải tiếp theo (lazy load, refresh) sử dụng loading indicator cục bộ (spinner). |

#### 3.3 Debounce Navigation & Khôi phục trạng thái khi mở lại app

- Khi người dùng tap nhanh liên tục (double tap) vào card hoặc các nút navigation (Quay lại...), hệ thống áp dụng cơ chế debounce để tránh mở trùng lặp màn hình.
- **Force close app** (tắt app không xóa dữ liệu) → Khi mở lại: giữ nguyên session đăng nhập, app quay về **Trang chủ** (không yêu cầu đăng nhập lại).
- **Uninstall app** → Khi cài lại: yêu cầu đăng nhập lại từ đầu. (Xem CMR-18)

#### 3.4 Đa ngôn ngữ (→ Xem CMR-17)

- **Text cứng ứng dụng:** Toàn bộ text cứng trên màn hình UC71-75 (header, tên mục hướng dẫn, placeholder, thông báo lỗi) được dịch sang ngôn ngữ hiển thị tương ứng khi người dùng đổi ngôn ngữ. Hỗ trợ 5 ngôn ngữ: VI, EN, ZH, JA, KO.
- **Nội dung CMS/API:** Nội dung hướng dẫn sử dụng (các bước thực hiện, note box) từ CMS/API **có hỗ trợ đa ngôn ngữ**. CMS quản lý nội dung theo từng ngôn ngữ. Khi người dùng đổi ngôn ngữ app → API trả về nội dung tương ứng với ngôn ngữ đã chọn.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Header màn hình chi tiết phải hiển thị đúng **tên danh mục hướng dẫn** tương ứng với Card đã chọn từ màn Hub (dynamic từ API, không hard-code).
- **AC2:** Nội dung hướng dẫn phải hiển thị **đầy đủ** theo cấu hình từ Admin Site — không bị cắt bớt, không có nút "Xem thêm".
- **AC3:** Nếu nội dung hướng dẫn dài hơn viewport, text phải **wrap** tự động và màn hình hỗ trợ cuộn dọc để xem toàn bộ.
- **AC4:** Khi mất kết nối mạng, App hiển thị thông báo lỗi + nút "Thử lại" (không crash, không blank screen).
- **AC5:** Hệ thống phải hỗ trợ cập nhật nội dung hướng dẫn từ phía Admin (Admin Site) mà không cần cập nhật lại phiên bản ứng dụng.
- **AC6:** Khi nội dung hướng dẫn null hoặc rỗng, hiển thị empty state *"Không có dữ liệu"* (CMR-14).

---

## 5. Lịch sử cập nhật

| Ngày      | Phiên bản  | Mục cập nhật                                         | Before                                                                                                                            | After                                                                                                                                       | Ghi chú                                                      |
| ---------- | ------------ | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 2026-05-16 | v1.0         | Khởi tạo tài liệu                                   | -                                                                                                                                 | Tách từ UC71-82 v2.2: tạo đặc tả riêng cho UC71-75 — Hướng dẫn sử dụng trên Mobile                                            | Tách UC theo yêu cầu BA                                    |
| 2026-05-18 | v1.0 → v1.1 | §3.1 step 2 — Loading state                           | "skeleton loading (placeholder nhấp nháy theo layout bước: 3-5 placeholder rows). Ẩn skeleton khi dữ liệu đã tải xong." | "loading indicator (spinner). Ẩn loading indicator khi dữ liệu đã tải xong."                                                          | Đồng bộ với UC2 — hệ thống không có skeleton loading |
| 2026-05-18 | v1.1 → v1.2 | §3.1 step 2 — Timeout                                 | (Không có)                                                                                                                      | "Tối đa 10 giây cho API. Quá 10 giây → Hiển thị 'Yêu cầu đã hết thời gian chờ. Vui lòng thử lại.' kèm nút 'Thử lại'." | Đồng bộ với UC2 — bổ sung timeout vào flow xử lý     |
| 2026-05-18 | v1.1 → v1.2 | §3.3 — Debounce Navigation & Khôi phục trạng thái | (Không có)                                                                                                                      | Bổ sung: debounce double-tap navigation; force close giữ session & quay về Trang chủ; uninstall → yêu cầu đăng nhập lại (CMR-18) | Đồng bộ với UC2/UC40                                      |
| 2026-05-18 | v1.2 → v1.3 | §2.2 — Cấu trúc màn hình Chi tiết                | Header cứng theo từng UC (A–E); Numbered Steps + Tab Bar + Banner giới thiệu                                                 | Header dynamic = tên danh mục hướng dẫn từ API; nội dung = text label hiển thị đầy đủ, wrap text nếu dài, không truncate    | Cập nhật theo wireframe thực tế                           |
| 2026-05-18 | v1.2 → v1.3 | §3.1 step 3 — Kiểu hiển thị nội dung              | "Nội dung dạng Numbered Steps — chỉ đọc, không tap, cuộn dọc"                                                            | "Nội dung dạng text label — wrap text nếu dài, hiển thị đầy đủ, cuộn dọc"                                                      | Cập nhật theo wireframe thực tế                           |
| 2026-05-18 | v1.2 → v1.3 | §4 — Acceptance Criteria                              | AC1–AC3 (bước cứng, lỗi mạng, admin CMS)                                                                                    | AC1–AC6: bổ sung AC header dynamic, wrap text, empty state null                                                                           | Cập nhật theo wireframe thực tế                           |
| 2026-05-18 | v1.3 → v1.4 | §2.1 row 5 — Grid Cards danh mục | (Không có rule tên dài) | Thêm: nếu tên danh mục quá dài → truncate với ellipsis (...) | Feedback BA |
| 2026-05-18 | v1.3 → v1.4 | §2.2 row 2 — Header tên danh mục | "Truncate nếu tên danh mục quá dài để vừa 1 dòng header" | "Nếu tên danh mục quá dài → wrap text" | Feedback BA |
| 2026-05-18 | v1.3 → v1.4 | §2.2 row 3 — Kiểu field nội dung | "Label (text thuần) — không phải Rich Text" | "Hỗ trợ Rich Text (bold, italic, ...) theo configuration từ Admin Site" | Feedback BA |
| 2026-05-18 | v1.3 → v1.4 | §2.2 row 3 — Gợi ý font/padding | "Font thường, line-height đủ rộng (gợi ý: 1.5–1.6). Padding trái/phải hợp lý (gợi ý: 16dp mỗi bên)." | (Đã xóa) | Feedback BA — không đặc tả UI cụ thể |
| 2026-05-18 | v1.4 → v1.5 | §1 Truy cập chức năng | Sidebar → "Hỗ trợ" → "Hướng dẫn sử dụng" | Bổ sung: Footer (Bottom Navigation) → Tab "Hướng dẫn sử dụng" | Cập nhật theo cấu trúc Footer mới (UC1 v4.2) |
| 2026-05-19 | v1.5 → v1.6 | §1 Truy cập chức năng (Sidebar) | Sidebar → "Hỗ trợ" → "Hướng dẫn sử dụng" | Sidebar → "Hướng dẫn sử dụng" (bỏ cấp "Hỗ trợ") | BA feedback — Sidebar trỏ thẳng |
| 2026-05-19 | v1.5 → v1.6 | §3.2 Xử lý lỗi | Bảng 3 cột (Tình huống / Thông báo / Hành vi) — 4 case | Bê nguyên bảng CMR-07 đầy đủ 6 case: Lỗi mạng, Lỗi 500, Lỗi 404, Lỗi 401, Timeout, Loading state | BA feedback — đảm bảo đủ case lỗi |
| 2026-05-21 | v1.6 → v1.7 | §2.1 row 5 — Grid Cards danh mục | (Không có empty state) | Bổ sung empty state: "Nếu danh sách từ API trả về rỗng (Admin chưa cấu hình), hiển thị thông báo 'Không có dữ liệu.' (theo chuẩn CMR-14)." | Feedback BA — Bổ sung empty state |
| 2026-05-21 | v1.7 → v1.8 | §3.1 step 4 — Pull to Refresh | (Không có) | Bổ sung: "Pull to Refresh (CMR-13): Kéo xuống từ đầu nội dung để tải lại dữ liệu từ CMS/API." | Align CMR-13 — đồng bộ với UC76-82, UC83-86 |
| 2026-05-21 | v1.7 → v1.8 | §2.1 Field #5, §2.2 Field #3, §4 AC6 — Empty state | `"Không có dữ liệu."` (có dấu `.`) | `"Không có dữ liệu"` (bỏ dấu `.`) | Đồng bộ CMR-14 / Section D — bỏ `.` theo hướng đồng bộ chung |
| 2026-05-21 | v1.7 → v1.8 | §3.2 — Nút "Thử lại" (Lỗi mạng & Timeout) | Chỉ ghi "Kèm nút Thử lại" — không mô tả loading state | Bổ sung: Tap "Thử lại" → nút chuyển sang loading state (disabled) trong khi gọi API → enabled lại sau khi API trả về | Đồng bộ CMR I08 |
