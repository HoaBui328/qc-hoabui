# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC76-82 — Câu hỏi thường gặp trên Mobile
**Ngày tạo:** 16/05/2026

| Thuộc tính              | Giá trị                                    |
| ------------------------- | -------------------------------------------- |
| Mã Use Case              | UC76, UC77, UC78, UC79, UC80, UC81, UC82     |
| Tên Use Case             | Câu hỏi thường gặp (FAQ)                  |
| BA phụ trách            | huy.lai2                                     |
| Giao diện                | Màn hình Mobile (Portrait)                 |
| Ngày tạo                | 16/05/2026                                   |
| Phiên bản               | v1.3                                         |

---

### 1. Mô tả chức năng

**Tên chức năng:** Câu hỏi thường gặp trên Mobile
**Mô tả:** Nhóm chức năng hỗ trợ người dùng tra cứu các câu hỏi thường gặp (FAQ). Phần FAQ hiển thị dạng **Grid Cards chủ đề** (chọn card chủ đề → lọc danh sách câu hỏi). Giúp người dùng tự giải quyết vướng mắc mà không cần liên hệ hỗ trợ.
**Phân quyền:** Cá nhân/Tổ chức (không yêu cầu đăng nhập — public access).
**Truy cập chức năng:** Sidebar → "Câu hỏi thường gặp".
**Phạm vi ngoài UC (Exclusions):** UC76-82 KHÔNG bao gồm: chỉnh sửa/quản lý nội dung FAQ (thuộc CMS Admin), gửi câu hỏi mới từ phía người dùng, đánh giá/rating mức độ hữu ích của câu trả lời FAQ, icon chuông thông báo (không có trên các màn hình UC76-82).
**Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
**Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị đầy đủ nội dung câu trả lời FAQ trên màn hình.
**Accessibility:** Touch target tối thiểu 44x44dp (theo platform guideline). Contrast ratio tuân theo WCAG 2.1 AA.
**Compatibility:** iOS 15+, Android 8.0+. Chỉ hỗ trợ Portrait.
**Chức năng đáp ứng usecase số:**
- UC76: Tra cứu câu hỏi thường gặp về thắc mắc chung trên mobile
- UC77: Tra cứu câu hỏi thường gặp về pháp lý và giấy tờ trên mobile
- UC78: Tra cứu câu hỏi thường gặp về thuế và tài chính trên mobile
- UC79: Tra cứu câu hỏi thường gặp về thủ tục hành chính trên mobile
- UC80: Tra cứu câu hỏi thường gặp về địa điểm và cơ sở hạ tầng trên mobile
- UC81: Tra cứu câu hỏi thường gặp về lao động và nhân sự
- UC82: Tra cứu câu hỏi thường gặp trên mobile

**Mapping UC76-81:** UC76 (FAQ — Thắc mắc chung), UC77 (FAQ — Pháp lý & giấy tờ), UC78 (FAQ — Thuế và tài chính), UC79 (FAQ — Thủ tục hành chính), UC80 (FAQ — Địa điểm & cơ sở hạ tầng), UC81 (FAQ — Lao động & nhân sự). Tất cả UC76-81 đều là **trạng thái lọc theo chủ đề** trên cùng một màn hình FAQ (UC82) — không phải màn hình riêng biệt. Mỗi UC tương ứng với việc tap chọn 1 Card chủ đề trên Grid Cards.

---

### 2. Giao diện người dùng (Mô tả chi tiết component)

#### 2.1 Màn hình Câu hỏi thường gặp (FAQ)

**Mô tả giao diện:**
Màn hình giúp người dùng lọc nhanh câu hỏi theo chủ đề hoặc tìm kiếm trực tiếp. UC76-81 đều là trạng thái lọc theo chủ đề trên cùng màn hình này.

| #  | Tên trường                        | Kiểu trường        | Giá trị mặc định                | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -- | ------------------------------------ | --------------------- | ------------------------------------ | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | Nút Quay lại (←)                  | Button (Icon)         | —                                   | —           | —         | **Quy tắc hiển thị:**<br>- Icon mũi tên ← căn trái trên header, màu trắng.<br>**Quy tắc hành động:**<br>- Tap → Quay về màn hình trước (Sidebar). (Xem CMR-06) |
| 2  | Tiêu đề Header                    | Label                 | "Câu hỏi thường gặp"            | —           | —         | **Quy tắc hiển thị:**<br>- Text "Câu hỏi thường gặp" căn giữa header, màu trắng trên nền đỏ đậm.<br>- Sticky — luôn hiển thị khi cuộn. |
| 3  | Label chọn chủ đề                | Label                 | "Chọn chủ đề"                    | —           | —         | **Quy tắc hiển thị:**<br>- Text "Chọn chủ đề", font đậm, căn giữa, nằm phía trên Grid Cards. |
| 4  | Grid Cards chủ đề                 | Card Grid (2 cột)    | Card "Tất cả" active               | —           | —         | **Quy tắc hiển thị:**<br>- Lưới 2 cột, **7 Cards:** Tất cả, Lao động & nhân sự, Địa điểm & cơ sở hạ tầng, Thuế và tài chính, Thủ tục hành chính, Pháp lý & giấy tờ, Câu hỏi chung.<br>- Mỗi Card: Icon minh họa + Tên chủ đề + Số lượng câu hỏi (**dynamic** từ API, format: "[N] câu hỏi"). N là số nguyên dương, format theo **CMR-11**. Số lượng được cập nhật cùng thời điểm tải danh sách (không realtime — chỉ refresh khi pull-to-refresh hoặc mở lại màn hình).<br>- Nếu chủ đề không có câu hỏi nào → Card vẫn hiển thị với text "0 câu hỏi". Không ẩn card. Khi tap → section danh sách hiển thị empty state "Không có dữ liệu." (CMR-14).<br>- **Active state:** Card đang chọn có **viền đỏ (border highlight)**. Mặc định: "Tất cả".<br><br>**Quy tắc hành động:**<br>- Tap Card → Lọc danh sách câu hỏi theo chủ đề. Ô tìm kiếm **reset rỗng**. Scroll **reset về đầu**. |
| 5  | Ô tìm kiếm                        | Textbox (Search)      | "Tìm kiếm nhanh theo câu hỏi, từ khoá" | x            | —         | **Quy tắc hiển thị:**<br>- Icon kính lúp bên trái. Tối đa **255 ký tự** (CMR-01).<br>**Quy tắc hành động:**<br>- Debounce 3 giây (CMR-01). Auto-trim whitespace (CMR-01).<br>- Người dùng có thể tìm kiếm nhanh theo **câu hỏi** hoặc **nội dung** của FAQ.<br>- **Phạm vi:** Chỉ tìm trong chủ đề đang chọn (exception CMR-01 vì Grid Cards không phải Tab). Khi ở "Tất cả" → tìm toàn bộ. |
| 6  | Section "Câu hỏi phổ biến nhất" | Section Header + List | —                                   | —           | —         | **Quy tắc hiển thị:**<br>- Header: Icon ⭐ + "Câu hỏi phổ biến nhất" (font đậm).<br>- **Chỉ hiển thị khi người dùng chọn "Tất cả"** — ẩn hoàn toàn khi chọn bất kỳ chủ đề cụ thể nào khác.<br>- Hiển thị tất cả câu hỏi được đánh dấu phổ biến từ mọi chủ đề, sắp xếp theo câu hỏi **0-9/A-Z**.<br>- Section này **không phân trang** — hiển thị toàn bộ (xem row 9). |
| 7  | Section danh sách câu hỏi          | Section Header + List | —                                   | —           | —         | **Quy tắc hiển thị:**<br>- Header: font đậm. **Header text thay đổi theo chủ đề đang chọn:**<br>&emsp;• Khi chọn "Tất cả" → Header hiển thị "Tất cả".<br>&emsp;• Khi chọn chủ đề cụ thể → Header hiển thị tên chủ đề đó (VD: "Thuế và tài chính", "Lao động & nhân sự").<br>- Hiển thị toàn bộ câu hỏi trong chủ đề đang chọn (bao gồm cả câu hỏi phổ biến — không loại trừ), sắp xếp theo câu hỏi **0-9/A-Z**.<br>- **Khi chọn chủ đề cụ thể:** Danh sách lọc theo chủ đề đó, áp dụng lazy load 20 items/lần (xem row 9).<br>- **Khi chọn "Tất cả":** Hiển thị toàn bộ câu hỏi từ mọi chủ đề, lazy load 20 items/lần. |
| 8  | Item câu hỏi                       | List Item (Card)      | —                                   | —           | —         | **Quy tắc hiển thị:**<br>- **Badge (tối đa 2):** (1) Badge trạng thái: "⭐ Phổ biến" (nền vàng, text nâu đậm) — chỉ hiển thị nếu câu hỏi được đánh dấu phổ biến từ CMS; nếu không → ẩn badge này. (2) Badge chủ đề: icon + tên chủ đề (nền màu theo chủ đề, text tương ứng). Badge nằm phía trên câu hỏi.<br>- **Nội dung câu hỏi:** Text câu hỏi hiển thị tối đa 3 dòng; nếu vượt quá → truncate với **...**<br>- **Icon điều hướng:** ">" bên phải.<br>- Nền trắng, bo góc.<br><br>**Quy tắc hành động:**<br>- Tap → Điều hướng sang màn hình Chi tiết câu trả lời.<br>- **Debounce Navigation (CMR-18):** Tap nhanh → chỉ nhận action đầu tiên. |
| 9  | Phân trang                          | Lazy Load             | 20 items/lần                        | —           | —         | CMR-04. Áp dụng cho section danh sách câu hỏi (row 7). Section "Câu hỏi phổ biến nhất" hiển thị toàn bộ (không phân trang).<br>**Lần tải đầu tiên:** Khi mở màn hình hoặc chọn chủ đề → tải 20 items (page 1), hiển thị loading indicator (spinner) trong khi chờ.<br>**Tải thêm:** Cuộn đến cuối → tự động tải 20 items tiếp theo. Hiển thị loading indicator (spinner) ở cuối danh sách.<br>**Kết thúc:** API trả về < 20 items hoặc rỗng → ẩn indicator, không gọi thêm.<br>**Chuyển chủ đề:** Phân trang reset về page 1, dữ liệu cũ bị xóa, tải lại 20 items đầu tiên của chủ đề mới.<br>**Lỗi load more:** Hiển thị nút "Tải lại" tại vị trí indicator, tap → retry cùng page. Dữ liệu đã tải giữ nguyên. |
| 10 | Empty state                          | Message               | —                                   | —           | —         | Tìm kiếm không có kết quả → *"Không tìm thấy kết quả."* (CMR-14).<br>Chủ đề không có câu hỏi → *"Không có dữ liệu."* (CMR-14). |

**Bảng mapping màu sắc và Icon chủ đề FAQ:**

| Chủ đề                | Icon | Màu nền Badge              | Màu Text Badge              |
| ------------------------ | ---- | ---------------------------- | ---------------------------- |
| Phổ biến               | ☆   | #FEF3C7 (Vàng nhạt)       | #92400E (Nâu đậm)        |
| Lao động & nhân sự   | 👥   | #F3F4F6 (Xám nhạt)        | #374151 (Xám đậm)        |
| Địa điểm & hạ tầng | 📍   | #F97316 (Cam)               | #FFFFFF (Trắng)            |
| Thuế và tài chính    | 💰   | #10B981 (Xanh lá)          | #FFFFFF (Trắng)            |
| Thủ tục hành chính   | 📋   | #C8102E (Đỏ)               | #FFFFFF (Trắng)            |
| Câu hỏi chung          | ❓   | #8B1A2B (Đỏ đậm)          | #FFFFFF (Trắng)            |
| Pháp lý & giấy tờ    | ⚖️ | #016630 (Xanh đậm)         | #FFFFFF (Trắng)            |

---

#### 2.2 Màn hình Chi tiết câu trả lời FAQ

**Mô tả giao diện:**
Màn hình tập trung vào việc đọc nội dung. Cần đảm bảo khoảng trắng (padding) hợp lý để người dùng dễ theo dõi.

1. **Header (Sticky):** Nền đỏ, nút Back (←) căn trái, tiêu đề "Câu hỏi thường gặp" căn giữa.
2. **Khu vực Nội dung (Scrollable):**
   - **Badges (tối đa 2):** Hiển thị ngay dưới Header, căn trái, cùng hàng ngang. (1) Badge trạng thái: "☆ Phổ biến" (nền vàng, text nâu đậm) — chỉ hiển thị nếu câu hỏi được đánh dấu phổ biến. (2) Badge chủ đề: icon + tên chủ đề (pill shape, bo góc tròn, sử dụng mapping màu sắc ở bảng mapping bên dưới).
   - **Tiêu đề câu hỏi:** Nằm dưới Badges. Font size lớn (VD: 18px-20px), font-weight: Bold. Màu đen (#000000). Padding-bottom: 16px.
   - **Đường kẻ phân cách:** Một đường kẻ mảnh (#E5E7EB) nằm ngang để tách biệt câu hỏi và câu trả lời.
   - **Nội dung câu trả lời:**
     - Sử dụng font thường, line-height cao (VD: 1.5 - 1.6) để dễ đọc.
     - Hỗ trợ hiển thị:
       - Văn bản thường.
       - Danh sách có dấu chấm đầu dòng (Bullet points).
       - Hình ảnh minh họa inline (nếu có): Căn giữa, bo góc nhẹ.
       - Link liên kết (xanh dương, có gạch chân).


| # | Tên trường                               | Kiểu trường         | Giá trị mặc định     | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------- | ---------------------- | ------------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nút Quay lại (←)                         | Button (Icon)          | —                        | —           | —         | Tap → Quay về màn hình FAQ UC82. (Xem CMR-06)                                                                                                                                                                                                                                                                          |
| 2 | Tiêu đề Header                           | Label                  | "Câu hỏi thường gặp" | —           | —         | Nằm giữa header, màu trắng trên nền đỏ.                                                                                                                                                                                                                                                                            |
| 3 | Badge trạng thái                          | Badge                  | —                        | —           | —         | **Quy tắc hiển thị:**<br>- "☆ Phổ biến" (nền vàng, text nâu đậm).<br>- Chỉ hiển thị nếu câu hỏi được đánh dấu phổ biến. Nếu không → ẩn badge này.<br>- Nằm cùng hàng với Badge chủ đề, căn trái.                                                                  |
| 4 | Badge chủ đề                             | Badge                  | —                        | —           | —         | **Quy tắc hiển thị:**<br>- Hiển thị badge chủ đề tương ứng (icon + text + màu theo bảng mapping màu sắc).<br>- Pill shape, bo góc tròn. Read-only.<br>- Luôn hiển thị.                                                                                                                   |
| 5 | Tiêu đề câu hỏi                        | Label                  | —                        | —           | —         | **Quy tắc hiển thị:**<br>- Font đậm, size lớn (18-20px), màu đen (#000000).<br>- Lấy từ API. Multi-line, không giới hạn số dòng (hiển thị đầy đủ).                                                                                                                                                                                 |
| 6 | Nội dung câu trả lời                    | Rich Text (Scrollable) | —                        | —           | —         | **Quy tắc hiển thị:**<br>- Nội dung từ API, hỗ trợ **Rich Text** (văn bản, bullet points, hình ảnh inline, link).<br>- Cuộn dọc toàn màn hình.<br>- **Empty state:** Nếu nội dung null → *"Không có dữ liệu."* (CMR-14).                                            |


---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý tra cứu FAQ

1. **Lọc theo chủ đề:** Khi người dùng tap vào một Card chủ đề → Card được chọn hiển thị **viền đỏ (active)**, hệ thống lọc danh sách câu hỏi bên dưới theo chủ đề đó.
   - **Section "Câu hỏi phổ biến nhất":** Chỉ hiển thị khi người dùng chọn "Tất cả" — ẩn hoàn toàn khi chọn chủ đề cụ thể.
   - **Section danh sách câu hỏi:** Header text thay đổi theo chủ đề đang chọn (VD: chọn "Thuế và tài chính" → header hiển thị "Thuế và tài chính"; chọn "Tất cả" → header hiển thị "Tất cả"). Hiển thị toàn bộ câu hỏi thuộc chủ đề đang chọn, lazy load 20 items/lần.
2. **Tìm kiếm (CMR-01):** Hệ thống lọc kết quả realtime theo từ khóa người dùng nhập vào ô tìm kiếm. **Phạm vi:** chỉ tìm kiếm trong chủ đề đang được chọn. Khi chọn "Tất cả" → tìm trên toàn bộ câu hỏi.
3. **Xem chi tiết:** Tap vào câu hỏi → Điều hướng sang màn hình chi tiết câu trả lời (Hỗ trợ định dạng Rich Text).
   - **Debounce Navigation (CMR-18):** Khi người dùng tap nhanh liên tục vào item câu hỏi, hệ thống chỉ nhận action đầu tiên và bỏ qua các tap tiếp theo cho đến khi điều hướng hoàn tất.
4. **Phân trang (CMR-04):** Danh sách FAQ sử dụng lazy load (infinite scroll), áp dụng cho section danh sách câu hỏi (row 7) (section "Câu hỏi phổ biến nhất" hiển thị toàn bộ, không phân trang).
   - **Lần tải đầu tiên:** Khi mở màn hình FAQ hoặc chọn chủ đề, hệ thống tải **20 items đầu tiên** (page 1). Trong khi chờ API → hiển thị **loading indicator** (spinner).
   - **Tải thêm (Load more):** Khi người dùng cuộn đến cuối danh sách (scroll position đạt threshold cuối) → tự động gọi API tải **20 items tiếp theo** (page 2, 3...). Hiển thị **loading indicator** (spinner) ở cuối danh sách trong khi chờ phản hồi.
   - **Kết thúc dữ liệu:** Khi API trả về ít hơn 20 items hoặc trả về rỗng → ẩn loading indicator, không gọi thêm API. Không hiển thị thông báo "Hết dữ liệu" (silent end).
   - **Lỗi khi tải thêm:** Nếu API lỗi khi load more → hiển thị nút **"Tải lại"** tại vị trí loading indicator. Tap → retry cùng page đó. Dữ liệu đã tải trước đó được giữ nguyên (không mất).
5. **Pull to Refresh (CMR-13):** Kéo xuống từ đầu danh sách FAQ để tải lại dữ liệu từ API/CMS.
6. **Chuyển chủ đề:** Khi người dùng tap vào Card chủ đề khác: (1) Ô tìm kiếm **reset về rỗng**. (2) Scroll position **reset về đầu danh sách**. (3) **Phân trang reset về page 1** — hệ thống gọi API tải 20 items đầu tiên của chủ đề mới (hiển thị loading indicator trong khi chờ). Dữ liệu chủ đề cũ bị xóa khỏi bộ nhớ hiển thị. (4) Nếu chủ đề mới không có câu hỏi → hiển thị empty state "Không có dữ liệu." (CMR-14). (5) Section "Câu hỏi phổ biến nhất" ẩn hoàn toàn khi chọn chủ đề cụ thể.
7. **Empty state (CMR-14):** Khi tìm kiếm/lọc FAQ không có kết quả → Hiển thị *"Không tìm thấy kết quả."*. Khi chủ đề không có câu hỏi nào → Hiển thị *"Không có dữ liệu."*.
8. **State preservation (CMR-01):** Khi user tap vào câu hỏi → xem chi tiết → tap Back quay lại màn FAQ: trạng thái chủ đề đang chọn, từ khóa tìm kiếm, và scroll position được giữ nguyên.

#### 3.2 Xử lý lỗi (→ Xem CMR-07)

| Quy tắc       | Mô tả                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lỗi mạng     | Hiển thị thông báo: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* Kèm nút "Thử lại".                                        |
| Lỗi API (500) | Hiển thị thông báo: *"Hệ thống đang bận. Vui lòng thử lại sau."*                                                                               |
| Lỗi 404       | Hiển thị: *"Nội dung không tồn tại hoặc đã bị xóa."*                                                                                           |
| Lỗi 401 (Session hết hạn) | Hệ thống sẽ tự động sử dụng **refresh token** để cấp lại access token mới. Nếu refresh token đã hết hạn hoặc không hợp lệ (quá **15 ngày**), người dùng sẽ được chuyển về **màn hình đăng nhập** và hiển thị **toast**: *"Phiên đăng nhập hết hạn."* |
| Timeout        | Nếu API không phản hồi trong **10 giây** → Hiển thị thông báo: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* Kèm nút "Thử lại". |
| Loading state  | Mọi API call phải có loading indicator trong khi chờ kết quả. Đối với **first-load** màn hình danh sách hoặc chi tiết, sử dụng **loading state toàn màn hình** (full-screen loading overlay). Các lần tải tiếp theo (lazy load, refresh) sử dụng loading indicator cục bộ (spinner). |

#### 3.3 Đa ngôn ngữ (→ Xem CMR-17)

- **Text cứng ứng dụng:** Toàn bộ text cứng trên màn hình UC76-82 (header, tên chủ đề, label, placeholder ô tìm kiếm, thông báo lỗi, empty state message) được dịch sang ngôn ngữ hiển thị tương ứng khi người dùng đổi ngôn ngữ. Hỗ trợ 5 ngôn ngữ: VI, EN, ZH, JA, KO.
- **Nội dung CMS/API:** Câu hỏi/câu trả lời FAQ từ CMS/API **có hỗ trợ đa ngôn ngữ**. CMS quản lý nội dung theo từng ngôn ngữ. Khi người dùng đổi ngôn ngữ app → API trả về nội dung tương ứng với ngôn ngữ đã chọn.

---

### 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Chức năng tìm kiếm FAQ phải trả về kết quả chính xác dựa trên cả tiêu đề câu hỏi và nội dung câu trả lời.
- **AC2:** Badge chủ đề trên mỗi câu hỏi FAQ phải hiển thị đúng màu sắc và nhãn theo quy định danh mục.
- **AC3:** Hệ thống phải hỗ trợ cập nhật nội dung FAQ từ phía Admin (CMS) mà không cần cập nhật lại phiên bản ứng dụng.
- **AC4:** Khi mất kết nối mạng, App hiển thị thông báo lỗi + nút "Thử lại" (không crash, không blank screen).
- **AC5:** Khi chủ đề FAQ không có câu hỏi hoặc tìm kiếm không có kết quả, App hiển thị empty state tương ứng (CMR-14).
- **AC6:** Lazy load FAQ áp dụng cho section danh sách câu hỏi (CMR-04): (1) Lần tải đầu tiên → tải 20 items (page 1), hiển thị loading indicator (spinner). (2) Cuộn đến cuối → tự động tải thêm 20 items, hiển thị spinner. (3) API trả về < 20 items hoặc rỗng → ẩn indicator, không gọi thêm. (4) Chuyển chủ đề → phân trang reset về page 1. (5) Lỗi khi load more → hiển thị nút "Tải lại", dữ liệu đã tải giữ nguyên.

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-16 | v1.0 | Khởi tạo tài liệu | - | Tách từ UC71-82 v2.2: tạo đặc tả riêng cho UC76-82 — Câu hỏi thường gặp trên Mobile | Tách UC theo yêu cầu BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 1,2,3 — Format mô tả | Mô tả ngắn, thiếu format | Bổ sung đầy đủ: Quy tắc hiển thị / hành động | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 4 — Số lượng [N] câu hỏi | (không gỏi CMR) | N là số nguyên dương, format theo CMR-11 | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 5 — Ô tìm kiếm | Placeholder "Tìm kiếm câu hỏi, từ khóa..."; tìm theo tiêu đề và câu trả lời | Placeholder "Tìm kiếm nhanh theo câu hỏi, từ khoá"; gỏi rõ: tìm theo câu hỏi hoặc nội dung FAQ | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 6 — Section phổ biến | Hiển thị cả khi chọn chủ đề cụ thể (giữ header, ẩn list) | Chỉ hiển thị khi chọn "Tất cả"; ẩn hoàn toàn khi chọn chủ đề cụ thể | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 6,7 — Sắp xếp | (không đề cập) | Sắp xếp theo câu hỏi 0-9/A-Z | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 8 — Truncate | "truncate với ellipsis (...)" | "truncate với **...**" | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.1 row 9 — Phân trang lần đầu | "skeleton loading" | "loading indicator (spinner)" | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §2.2 — Footer + Row 7 | Có nút "👍 Tôi thấy thông tin này hữu ích" | Xóa hoàn toàn Footer và Row 7 | Feedback BA |
| 2026-05-18 | v1.0 → v1.1 | §4 AC6,AC7 | AC6: nút hữu ích; AC7: skeleton loading | Xóa AC6 cũ; cập nhật AC6 mới: lazy load + loading indicator | Feedback BA |
| 2026-05-19 | v1.1 → v1.2 | §1 Truy cập chức năng (Sidebar) | Sidebar → "Hỗ trợ" → "FAQ" | Sidebar → "Câu hỏi thường gặp" (bỏ cấp "Hỗ trợ", đổi label) | BA feedback — Sidebar trỏ thẳng |
| 2026-05-19 | v1.1 → v1.2 | §3.2 Xử lý lỗi | Bảng 3 cột (Tình huống / Thông báo / Hành vi) — 4 case | Bê nguyên bảng CMR-07 đầy đủ 6 case: Lỗi mạng, Lỗi 500, Lỗi 404, Lỗi 401, Timeout, Loading state | BA feedback — đảm bảo đủ case lỗi |
| 2026-05-21 | v1.2 → v1.3 | §2.1 row 5 — Ô tìm kiếm max length | Tối đa **500 ký tự** (CMR-01) | Tối đa **255 ký tự** (CMR-01) | Align CMR Mobile v6.1 — rule E05/G05 |
