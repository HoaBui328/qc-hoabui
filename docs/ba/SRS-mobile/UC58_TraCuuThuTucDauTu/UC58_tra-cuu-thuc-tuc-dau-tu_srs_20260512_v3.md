# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC58 — Tra cứu thủ tục đầu tư trên Mobile  
**Ngày tạo:** 12/05/2026  
**Phiên bản:** v3.5

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | hieu.luu2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Tra cứu thông tin thủ tục đầu tư |
| Đối tượng thực hiện | Nhà đầu tư (Cá nhân / Tổ chức) |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 12/05/2026 |
| Phiên bản | v3.5 |

---

## UC58 — Tra cứu thủ tục đầu tư trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu thủ tục đầu tư
- **Mô tả:** Chức năng cho phép người dùng (nhà đầu tư) tìm kiếm, lọc và tra cứu thông tin chi tiết về các thủ tục liên quan đến đầu tư. Người dùng có thể tìm kiếm theo từ khóa, lọc theo lĩnh vực, cấp thực hiện, mức độ, và thời gian. Màn hình chi tiết hiển thị tổng quan thông tin thủ tục, phí, lệ phí, căn cứ pháp lý, quy trình thực hiện (timeline) và các thành phần hồ sơ yêu cầu (bắt buộc/tùy chọn).
- **Phân quyền:** Cá nhân/Tổ chức (Không yêu cầu đăng nhập — public access).
- **Phạm vi ngoài UC (Exclusions):** N/A.
- **Truy cập chức năng:** Trang chủ → "Thủ tục đầu tư".
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị kết quả danh sách thủ tục đầu tư hoặc chi tiết thủ tục theo điều kiện của người dùng.
- **Chức năng đáp ứng usecase số:** UC58

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Thủ tục về đầu tư

**Mô tả giao diện:**
Header nền đỏ đậm, ô tìm kiếm và nút Bộ lọc. Ngay dưới ô tìm kiếm là nhãn "Hiển thị [N] kết quả" kèm theo các tag bộ lọc hiện tại. Bên dưới là danh sách kết quả dạng Vertical List Card.

**Khung Header & Tìm kiếm:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại & Tiêu đề | Button (Icon) & Label | "Thủ tục về đầu tư" | — | — | **Quy tắc hiển thị:** Header màu đỏ đậm, chữ trắng.<br>**Quy tắc hành động:** Tap icon (←) → Quay về màn hình trước (CMR-06). |
| 2 | Icon Thông báo | Button (Icon) | — | — | — | **Quy tắc hiển thị:** Góc phải header (icon chuông có chấm đỏ).<br>**Quy tắc hành động:** Tap → Chuyển đến màn hình Thông báo. |
| 3 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm nhanh theo tên thủ tục" | x | — | **Quy tắc hiển thị:** Tối đa **255 ký tự** (Tham chiếu CMR-01).<br><br>**Quy tắc hành động:**<br>- Nhập từ khóa → Hệ thống tìm kiếm theo tên hoặc mã thủ tục sau **debounce 3 giây** (CMR-01).<br>- Xử lý auto-trim khoảng trắng đầu/cuối (CMR-01).<br>- State Persistence: Giữ nguyên từ khóa khi quay lại từ màn hình chi tiết (CMR-01). |
| 4 | Nút Bộ lọc | Button (Icon) | — | — | — | **Quy tắc hiển thị:** Icon filter màu trắng, bo góc đỏ đậm, nằm bên phải ô tìm kiếm.<br>- **Active filter indicator:** Nếu đang áp dụng bộ lọc (khác mặc định), hiển thị chấm báo hiệu (CMR-02).<br>**Quy tắc hành động:** Tap → Mở Modal popup "Bộ lọc tìm kiếm". |
| 5 | Dòng tóm tắt kết quả & Tag | Label Group | — | — | — | **Quy tắc hiển thị:**<br>- Text xám: "Hiển thị **[N]** kết quả" (với N là số lượng).<br>- Tag bộ lọc: Hiển thị các tiêu chí đang được áp dụng dưới dạng badge (VD: Nền đỏ nhạt chữ đỏ "Đầu tư"). |

**Khung Danh sách kết quả (Card):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Danh sách Card thủ tục | List Card (Vertical) | — | — | — | **Quy tắc hiển thị:** Cuộn dọc, lazy load 20 item/lần. Trạng thái Empty hiển thị "Không tìm thấy kết quả." (CMR-14).<br>**Quy tắc hành động:** Hỗ trợ Pull to Refresh (CMR-13). |
| 7 | Tên thủ tục | Label (H3) | — | — | — | **Quy tắc hiển thị:** Font đậm, chữ đen, tối đa 2 dòng (quá 2 dòng hiển thị `...`). |
| 8 | Thuộc tính thủ tục | Label / Value | — | — | — | **Quy tắc hiển thị:** Gồm: Mã thủ tục (VD: TT-DT-01), Lĩnh vực (VD: Đầu tư), Cơ quan (VD: Bộ KH&ĐT). Value trống hiển thị "-". |
| 9 | Tương tác thẻ (Xem chi tiết) | Interaction | — | — | — | **Quy tắc hành động:** Tap vào toàn bộ thẻ → Mở màn hình Chi tiết thủ tục. Áp dụng Debounce Navigation (CMR-18). |

---

#### 2.2 Bottom Sheet Bộ lọc tìm kiếm

**Mô tả giao diện:**
Dạng Bottom Sheet (Modal). Đóng khi tap ra ngoài.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Đóng (X) & Tiêu đề | Button (Icon) & Label | "Bộ lọc tìm kiếm" | — | — | **Quy tắc hiển thị:** Tiêu đề ở giữa, nút (X) bên phải.<br>**Quy tắc hành động:** Tap (X) hoặc tap vùng xám → Đóng, không lưu. |
| 2 | Lĩnh vực | Searchable Dropdown (Single) | "Chọn lĩnh vực" | x | — | **Quy tắc hiển thị:** Option lấy từ API (Tham chiếu CMR-03).<br>**Hành vi clear keyword (D07/D08):** Xóa hết keyword → hiển thị placeholder "Chọn lĩnh vực". Tap ra ngoài khi trống → giữ giá trị rỗng, trigger validation nếu bắt buộc. |
| 3 | Cấp thực hiện | Searchable Dropdown (Single) | "Tất cả" | x | — | **Quy tắc hiển thị:** Option lấy từ API (Tham chiếu CMR-03).<br>**Hành vi clear keyword (D07/D08):** Xóa hết keyword → hiển thị placeholder "Tất cả". Tap ra ngoài khi trống → chọn lại "Tất cả". |
| 4 | Mức độ | Searchable Dropdown (Single) | "Tất cả" | x | — | **Quy tắc hiển thị:** Option lấy từ API (Tham chiếu CMR-03).<br>**Hành vi clear keyword (D07/D08):** Xóa hết keyword → hiển thị placeholder "Tất cả". Tap ra ngoài khi trống → chọn lại "Tất cả". |
| 5 | KHOẢNG THỜI GIAN | Date Picker Range | "dd/mm/yyyy" | x | — | **Quy tắc hiển thị:** Gồm 2 trường: "Từ ngày" và "Đến ngày" kèm icon lịch.<br>**Quy tắc hành động:** Kiểm tra hợp lệ thời gian (Từ ngày <= Đến ngày) theo quy chuẩn CMR-15.<br>**Error:** Nếu Từ ngày > Đến ngày → hiển thị inline error: `"Từ ngày không được lớn hơn Đến ngày!"` |
| 6 | Nhóm "Bộ lọc đang áp dụng" | Badge Group | — | — | — | **Quy tắc hiển thị:** Vùng có viền nét đứt. Các tiêu chí đã chọn ở trên tự động sinh ra các tag màu nhạt (VD: "Tất cả lĩnh vực", "Toàn trình"). |
| 7 | Nút "Thiết lập lại" | Button (Outline) | — | — | — | **Quy tắc hiển thị:** Viền xám, kèm icon refresh.<br>**Quy tắc hành động:** Tap → Reset các dropdown và ngày tháng về mặc định. |
| 8 | Nút "Áp dụng" | Button (Primary) | — | — | — | **Quy tắc hiển thị:** Nền đỏ đậm, chữ trắng. **Luôn Enabled** (CMR-09). Không có trạng thái Disabled.<br>**Quy tắc hành động:** Tap → Đóng Bottom Sheet và call API tải lại danh sách kết quả. |

---

#### 2.3 Màn hình Chi tiết Thủ tục hành chính

**Mô tả giao diện:**
Gồm khối thôngู Highlight (Thời hạn, Cấp, Đối tượng) và thanh Tab bar chia làm 3 tab: Thông tin chung, Trình tự thực hiện, Thành phần hồ sơ.

**Khung Header & Thông tin tổng quan:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Header (Back & Chuông) | Button | "Chi tiết thủ tục" | — | — | **Quy tắc hiển thị:** Header đỏ đậm, chữ trắng. |
| 2 | Nhóm Tag thủ tục | Badge Group | — | — | — | **Quy tắc hiển thị:** Nằm dưới header, bo góc, viền đỏ mờ. Gồm: `# Mã_Thủ_Tục`, `Tên_Lĩnh_Vực`, `Mức_Độ_Dịch_Vụ` (Màu sắc badge phụ thuộc loại mức độ). |
| 3 | Tên thủ tục (Highlight) | Label (H2) | — | — | — | **Quy tắc hiển thị:** Font chữ lớn, in đậm, màu trắng trên nền đỏ. |
| 4 | 3 Box Highlight thông tin | Card Box | — | — | — | **Quy tắc hiển thị:** 3 ô vuông xếp ngang, bo góc, nền đỏ sậm trong khu vực header đỏ. Bao gồm thông số (chữ to) và Label (chữ nhỏ):<br>- **Thời hạn** (VD: 15 ngày)<br>- **Cấp thực hiện** (VD: Cấp tỉnh)<br>- **Đối tượng** (VD: Cá nhân / TC) |
| 5 | Tab Bar (3 Tabs) | Tab Group | "Thông tin chung" | — | — | **Quy tắc hiển thị:** 3 tab: **Thông tin chung**, **Trình tự thực hiện**, **Thành phần hồ sơ**.<br>**Quy tắc hành động:** Chuyển đổi tab bằng cách tap trực tiếp vào tên tab hoặc vuốt ngang màn hình (Swipe left/right). |

**Nội dung Tab 1: Thông tin chung:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Block Thông tin thủ tục | List Attribute | — | — | — | **Quy tắc hiển thị:** Gồm cặp Nhãn/Giá trị: Thời hạn giải quyết, Cơ quan thực hiện, Lĩnh vực, Cấp thực hiện, Đối tượng thực hiện, Kết quả. |
| 7 | Block Phí & Lệ phí | List Attribute | — | — | — | **Quy tắc hiển thị:** Cặp Nhãn/Giá trị:<br>- **Phí thẩm định**: (VD: "Không" — chữ in đậm màu xanh lá).<br>- **Lệ phí cấp phép**: (VD: "500.000 đ" — chữ in đậm màu đỏ). **Phải fomat định dạng tiền tệ có dấu phẩy/chấm theo chuẩn CMR-11**. |
| 8 | Block Căn cứ pháp lý | List (Icon) | — | — | — | **Quy tắc hiển thị:** Mỗi dòng là 1 luật/nghị định, có icon mũi tên `>`.<br>- Tên luật in đậm đỏ (VD: Luật Đầu tư 2020).<br>- Mô tả trích yếu xám mờ ở dưới.<br>**Quy tắc hành động:** Đây chỉ là danh sách **hiển thị nội dung tĩnh** (không mở link trình duyệt, không tap để xem chi tiết văn bản). |

**Nội dung Tab 2: Trình tự thực hiện:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 9 | Label Tổng thời gian | Label Box | — | — | — | **Quy tắc hiển thị:** Box viền đỏ mờ. Nội dung: "Tổng thời gian xử lý: **[X] ngày làm việc** kể từ ngày nhận đủ hồ sơ hợp lệ." |
| 10 | Timeline các bước (Quy trình) | Vertical Timeline | — | — | — | **Quy tắc hiển thị:** Trục thời gian dọc nối các bước bằng vòng tròn số (01, 02, 03, 04...). Mỗi bước có:<br>- **Tên bước** (In đậm).<br>- **Mô tả hành động**: Cho phép cuộn hiển thị text dài vô tận (tự động giãn dòng), không giới hạn ký tự và không dùng nút "Xem thêm".<br>- **Tag Thời hạn** (VD: 1 ngày).<br>- **Tag Đối tượng phụ trách** (VD: Nhà đầu tư / Sở KH&ĐT).<br>Màu sắc vòng tròn số và tag thay đổi tùy vào từng bước thực hiện. |

**Nội dung Tab 3: Thành phần hồ sơ:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 11 | Summary Header | Label Box | — | — | — | **Quy tắc hiển thị:** Box nền xám mờ. Nội dung: "Tổng cộng **X** thành phần hồ sơ — **Y bắt buộc**, **Z tùy chọn**." |
| 12 | Khối "Tài liệu bắt buộc" | List Group | — | — | — | **Quy tắc hiển thị:**<br>- Header viền đỏ mờ, có icon và số lượng Y trên badge đỏ đậm.<br>- Danh sách đánh số tự động.<br>- Mỗi thẻ tài liệu gồm: Tên tài liệu (In đậm), Diễn giải, Tag **Bản chính: [Số]**, Tag **Bản sao: [Số]**, Tag **"Bắt buộc"** nền đỏ mờ. |
| 13 | Khối "Tài liệu tùy chọn" | List Group | — | — | — | **Quy tắc hiển thị:**<br>- Header viền vàng mờ, có icon và số lượng Z trên badge vàng sậm.<br>- Đánh số tiếp nối từ danh sách trên.<br>- Mỗi thẻ tương tự Bắt buộc, nhưng Tag trạng thái cuối đổi thành **"Tùy chọn"** nền vàng nhạt. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng xem danh sách và tìm kiếm
1. Truy cập chức năng "Thủ tục về đầu tư". Gọi API lấy danh sách. Nếu API trả về danh sách rỗng → hiển thị "Không có dữ liệu." (CMR-14). Nếu search/filter không có kết quả → hiển thị "Không tìm thấy kết quả." (CMR-14).
2. Ô tìm kiếm kích hoạt gọi API với **debounce 3 giây** (CMR-01). Hệ thống tự động loại bỏ khoảng trắng đầu/cuối của từ khóa.
3. Chức năng Lọc: Bottom Sheet cho phép áp dụng đồng thời các filter (Lĩnh vực, Cấp thực hiện, Mức độ, Từ ngày - Đến ngày theo CMR-15). Khi bấm "Áp dụng", list sẽ refresh và các tag trạng thái bộ lọc trên UI được cập nhật realtime, kèm text "Hiển thị [N] kết quả".
4. Lazy loading: Cuộn để tải thêm mỗi lần 20 item. **Lưu ý:** Nếu lỗi mạng hoặc timeout khi lazy load, hệ thống tự động **retry 3 lần ngầm** (mỗi lần cách 2s) trước khi hiển thị Toast lỗi hoặc Footer error state (CMR-04).
5. State Persistence (CMR-01): Khi xem chi tiết rồi ấn nút Quay lại, hệ thống ghi nhớ chính xác trạng thái tìm kiếm, lọc và vị trí thanh cuộn.
6. Tap vào toàn bộ thẻ sẽ vào Màn hình chi tiết (chống click double bằng debounce CMR-18).

#### 3.2 Luồng xem chi tiết
1. Hệ thống gọi API lấy chi tiết bằng ID thủ tục. Trong khi tải sẽ hiển thị Skeleton Loading.
2. Xử lý **Partial API Failure** (CMR-07): Nếu API của 3 khối (Thông tin chung, Trình tự, Hồ sơ) là các endpoints riêng biệt hoặc có cơ chế bóc tách lỗi, khi 1 phần lỗi (VD: API thành phần hồ sơ timeout) thì các phần khác vẫn render bình thường, phần lỗi sẽ hiển thị box "Không tải được dữ liệu, thử lại".
3. Dữ liệu Phí / Lệ phí trả về (số) phải được phía Client parse theo chuẩn định dạng dấu phân cách (CMR-11).
4. Người dùng vuốt màn hình (Swipe left/right) hoặc tap trên thanh Tab Bar để chuyển đổi nội dung 3 Tab. Dữ liệu có thể được lazy load hoặc render 1 lần từ đầu tùy API response.

#### 3.3 Xử lý session
- **Session Expire:** Reference theo chuẩn hệ thống chung (UC1) - nếu API cần token trả về 401. Nhưng do là public access, user chưa login vẫn có thể xem được bình thường.

#### 3.4 Xử lý lỗi (Tham chiếu CMR-07)
| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
| --- | --- | --- |
| Lỗi mạng (Network Drop) | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* | Giữ nguyên dữ liệu cũ, hiển thị pop-up hoặc Toast kèm nút "Thử lại". |
| Không có kết quả sau lọc | *"Không tìm thấy kết quả."* | Hiển thị Empty state, ẩn danh sách (CMR-14). |
| Timeout API (Quá 10s) | *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại"* | Timeout tiêu chuẩn của API là 10 giây (CMR-16). |

#### 3.5 Tiêu chí chấp nhận (Acceptance Criteria)
- **AC1:** Tính năng tìm kiếm hoạt động với debounce 3 giây và auto-trim khoảng trắng (CMR-01).
- **AC2:** Lọc dữ liệu qua Bottom Sheet hoạt động chính xác. Ngày tháng áp dụng quy tắc valid date range (Từ ngày <= Đến ngày) (CMR-15).
- **AC3:** UI danh sách hiển thị đúng Lazy load 20 item (có cơ chế tự retry ngầm 3 lần khi lỗi - CMR-04), Pull to Refresh (CMR-13), và Text thống kê "Hiển thị [N] kết quả" + Tag bộ lọc động.
- **AC4:** Tap Card chuyển sang màn hình Chi tiết mượt mà (debounce chống double tap - CMR-18).
- **AC5:** Màn hình chi tiết hiển thị đúng layout 3 Tabs, cho phép thao tác vuốt ngang Swipe chuyển tab.
- **AC6:** Các box Highlight (15 ngày, cấp tỉnh) lấy đúng data. Phí và lệ phí hiển thị chuẩn format tiền tệ VNĐ (CMR-11).
- **AC7:** Tab Trình tự hiển thị đúng UI Vertical Timeline, thay đổi màu sắc Node số thứ tự và Tag. Cấu trúc thẻ mô tả nội dung tự động giãn dòng vô tận khi text dài.
- **AC8:** Tab Thành phần hồ sơ đếm số liệu chuẩn xác ("4 bắt buộc, 2 tùy chọn"), phân rõ 2 nhóm và tag đánh dấu bản sao/bản chính.
- **AC9:** State persistence: Các trạng thái list (Search, Filter, Scroll position) đều được giữ nguyên khi user điều hướng trở về từ màn hình chi tiết (CMR-01).

#### 3.6 Đa ngôn ngữ (→ Xem CMR-17)
- Hệ thống hỗ trợ đa ngôn ngữ. Các nhãn tĩnh (text cứng) như "Thông tin chung", "Thành phần hồ sơ", "Phí & lệ phí", "Bản chính", "Bản sao"... được thay đổi ngôn ngữ ngay lập tức theo cài đặt của hệ điều hành. **Setting ngôn ngữ này được lưu trữ và đồng bộ hóa thông qua API (không chỉ lưu ở Local Storage).**
- Nội dung từ API (Tên thủ tục, Mô tả luật, Tên bước thực hiện) hiển thị nguyên gốc hoặc trả về dạng localization array (nếu API có hỗ trợ).

---

### 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 12/05/2026 | v1.0 | Tạo mới | (Không có) | Tạo mới tài liệu SRS UC58 | Thiết kế theo wireframe mới. Đồng bộ với CMR chuẩn dự án. |
| 12/05/2026 | v2.0 | Cập nhật UI Card | Có nút "Nộp hồ sơ" | Xóa nút "Nộp hồ sơ", tap vào toàn thẻ để xem chi tiết | Phù hợp với scope Tra cứu của UC |
| 12/05/2026 | v3.0 | Giải đáp Audit (Gap) | Chưa rõ hành vi chi tiết | Làm rõ: Căn cứ pháp lý là text tĩnh, Timeline cuộn dọc dài vô tận, Ngôn ngữ đồng bộ API. | Dựa trên kết quả QnA |
| 2026-05-21 | v3.0 → v3.1 | Align CMR Mobile v6.0 | 1. Search box max length 500→255. 2. Bổ sung CMR-03 cho Searchable Dropdown. |
| 2026-05-21 | v3.1 → v3.2 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v3.2 → v3.3 | Nút "Áp dụng" filter | (Chưa tường minh trạng thái) | Bổ sung: **Luôn Enabled** (CMR-09). Không có trạng thái Disabled. | Đồng bộ CMR-09 |
| 2026-05-21 | v3.3 → v3.4 | Sửa kiểu trường Dropdown → Searchable Dropdown (Lĩnh vực, Cấp thực hiện, Mức độ) | `Dropdown (Single)` — chỉ ghi "(Tham chiếu CMR-03)" | `Searchable Dropdown (Single)` — bổ sung mô tả hành vi D07/D08 cụ thể | Align CMR v6.0 rule D07/D08 |
| 2026-05-21 | v3.3 → v3.4 | Bổ sung error message Date Validation (Khoảng thời gian) | Chỉ ghi "Kiểm tra hợp lệ thời gian theo CMR-15" — không có error message | Bổ sung: `"Từ ngày không được lớn hơn Đến ngày!"` | Đồng bộ format error có `!` theo CMR H03/H04 |
| 2026-05-22 | v3.4 → v3.5 | §2.2 — Lĩnh vực: Placeholder | `"Chọn lĩnh vực đầu tư"` | `"Chọn lĩnh vực"` | Align CMR-03 format "Chọn [tên trường]" |
| 2026-05-22 | v3.4 → v3.5 | §2.2 — Cấp thực hiện: Giá trị mặc định | `"Tất cả các cấp"` | `"Tất cả"` | Align CMR-03 filter dropdown mặc định "Tất cả" |
| 2026-05-22 | v3.4 → v3.5 | §2.2 — Mức độ: Giá trị mặc định | `"Dịch vụ công toàn trình"` | `"Tất cả"` | Align CMR-03 filter dropdown mặc định "Tất cả" |
| 2026-05-22 | v3.4 → v3.5 | §3.4 — Timeout message | `"Máy chủ phản hồi chậm. Vui lòng thử lại sau."` | `"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại"` | Align CMR-07 timeout message chuẩn |
| 2026-05-22 | v3.4 → v3.5 | §3.1 step 1 — Empty state | `"Nếu trống thì hiển thị theo CMR-14 ("Không tìm thấy kết quả.")"` | Phân biệt: API rỗng → "Không có dữ liệu." / Search-filter không kết quả → "Không tìm thấy kết quả." | Align CMR-14 phân biệt no data vs no result |
