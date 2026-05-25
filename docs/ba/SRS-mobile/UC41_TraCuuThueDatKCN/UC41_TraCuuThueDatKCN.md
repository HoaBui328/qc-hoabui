# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC41 — Tra cứu thông tin cho thuê đất trong Khu công nghiệp trên Mobile
**Ngày tạo:** 16/05/2026

| Thuộc tính              | Giá trị                         |
| ------------------------- | --------------------------------- |
| BA phụ trách            | han.luong                         |
| Phân hệ                 | Ứng dụng Di động (Mobile App) |
| Loại chức năng         | Khai thác thông tin KCN/KKT     |
| Đối tượng thực hiện | Cá nhân / Tổ chức             |
| Giao diện                | Màn hình Mobile (Portrait)      |
| Ngày tạo                | 16/05/2026                        |
| Phiên bản               | v1.7                                |

---

## UC41 — Tra cứu thông tin cho thuê đất trong KCN trên Mobile

### 1. Mô tả chức năng

**Tên chức năng:** Tra cứu thông tin cho thuê đất trong khu công nghiệp trên Mobile
**Mô tả:** Chức năng cho phép cá nhân, tổ chức tra cứu danh sách các hợp đồng cho thuê đất trong các khu công nghiệp. Người dùng có thể tìm kiếm theo từ khóa (số hợp đồng, tên lô), lọc theo nhiều tiêu chí (nhà đầu tư, KCN, tình trạng hợp đồng, ngày ký, v.v.), và xem thông tin chi tiết từng hợp đồng.
**Phân quyền:** Tất cả cá nhân/tổ chức đã đăng nhập thành công đều được truy cập.
**Truy cập chức năng:** Sidebar → "Thông tin cho thuê đất".
**Chức năng đáp ứng usecase số:** UC41 (WBS Mobile — STT 41)

**Phạm vi ngoài (Out-of-scope):**
- Không cho phép tạo mới thông tin cho thuê đất.
- Không cho phép chỉnh sửa thông tin cho thuê đất.
- Không cho phép xóa thông tin cho thuê đất.
- Không cho phép export dữ liệu.
- Không cho phép in (print).

---

### 2. Mô tả giao diện

#### 2.1 Giao diện Danh sách thông tin cho thuê đất

**Mô tả giao diện:**
Màn hình tiêu đề "Thông tin cho thuê đất". Phía dưới header là thanh tìm kiếm kết hợp bộ lọc tìm kiếm. Nội dung là danh sách Card thông tin hợp đồng cho thuê đất, hiển thị tóm tắt các thông tin chính, badge trạng thái hợp đồng, và các nút hành động nhanh.

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường       | Giá trị mặc định                       | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------- | -------------------- | ------------------------------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Ô tìm kiếm | Textbox (Search)     | Placeholder: "Tìm kiếm nhanh theo số hợp đồng, tên lô" | x            | -         | **Quy tắc hiển thị:**<br>- Tìm kiếm like theo số hợp đồng và tên lô đất.<br>- Tìm kiếm gần đúng (chứa từ khóa). Khi xóa hết từ khóa, danh sách trở về trạng thái mặc định (hiển thị tất cả).<br><br>**Quy tắc hành vi:**<br>- Debounce 3 giây: hiển thị kết quả tìm kiếm trong lúc gõ, sau 3 giây không gõ mới thực hiện tìm kiếm.<br>- Người dùng nhập từ khóa → Kết quả hiển thị ngay (sau debounce), không cần nhấn Enter hay nút Tìm kiếm.<br>- Tự động trim space (cắt khoảng trắng hai đầu) trước khi tìm kiếm. Nếu sau trim rỗng → không trigger search, danh sách về mặc định.<br>- Nếu không có kết quả trùng khớp: Hiển thị *"Không tìm thấy kết quả."* ở giữa vùng nội dung. Không có action Thử lại vì không phải lỗi.<br>- Max length: **255 ký tự** (Xem CMR-01). Khi nhập đủ 255 ký tự, không cho phép nhập thêm.<br>- Xem CMR-01 |
| 2 | Nút "Lọc"   | Button (Icon Filter) | -                                          | —           | -         | **Quy tắc hiển thị:**<br>- Icon filter nằm bên phải ô tìm kiếm.<br>- Nếu có filter active (giá trị khác mặc định) → hiển thị **icon indicator màu xanh lá cây** ở góc phải bên trên của icon filter theo CMR-02. Khi reset filter → ẩn indicator.<br><br>**Quy tắc hành động:**<br>- Tap → Mở Bottom Sheet bộ lọc tìm kiếm.<br>- Tap 'Áp dụng' / 'Tìm' → Đóng bộ lọc, tải lại danh sách với tiêu chí đã chọn.<br>- Tap 'Đặt lại' / 'Nhập lại' → Reset tất cả trường về giá trị mặc định (không đóng sheet).<br>- Tap vùng ngoài, nút 'Đóng' (X), hoặc nút 'X' góc phải → Đóng bộ lọc, không thay đổi kết quả hiện tại. |

**Khung Modal Bộ lọc tìm kiếm (Bottom Sheet):**

> Bộ lọc được hiển thị dưới dạng Bottom Sheet. Người dùng chỉnh sửa các tiêu chí trong sheet, sau đó tap "Áp dụng" để áp dụng. Tất cả các trường lọc (trừ Date) đều là **single-selection** (chỉ chọn một giá trị một lần). Bottom Sheet có nút "X" ở góc phải trên cùng để đóng.

| # | Tên trường           | Kiểu trường                          | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------- | --------------------------------------- | --------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nhà đầu tư thuê đất | Dropdown (Single-selection, Searchable) | Tất cả | x            | -         | **Quy tắc hiển thị:**<br>- Placeholder: "Chọn nhà đầu tư thuê đất". Hiển thị placeholder khi option được clear.<br>- Danh sách nhà đầu tư lấy từ API. Mặc định: "Tất cả".<br>- **Searchable dropdown**: Cho phép người dùng nhập từ khóa để tìm kiếm trong danh sách (tìm kiếm gần đúng, sắp xếp A-Z). Chi tiết xem CMR-03.<br><br>**Quy tắc hành động:**<br>- Chọn một nhà đầu tư cụ thể để lọc. Giá trị "Tất cả" là tùy chọn mặc định — không áp dụng lọc.<br>- Tap → Mở danh sách lựa chọn (có ô search) → Nhập từ khóa để lọc option → Tap item → Tự động đóng và hiển thị giá trị đã chọn.<br>- Option đã chọn được highlight/bold khi mở lại dropdown. (Xem CMR-03)<br>- Nếu đang ở trạng thái clear (hiển thị placeholder) mà người dùng tap ra ngoài → tự động chọn lại "Tất cả".               |
| 2 | Tình trạng hợp đồng  | Dropdown (Single-selection)             | Tất cả | x            | -         | **Quy tắc hiển thị:**<br>- Lọc theo tình trạng của hợp đồng.<br><br>**Quy tắc hành động:**<br>- Các giá trị có thể chọn: **Tất cả** (mặc định — không lọc) / **Đang cho thuê** / **Hết hạn** / **Thu hồi** / **Khác**.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 3 | Khu công nghiệp       | Dropdown (Single-selection, Searchable) | Tất cả | x            | -         | **Quy tắc hiển thị:**<br>- Placeholder: "Chọn khu công nghiệp". Hiển thị placeholder khi option được clear.<br>- Danh sách các KCN lấy từ API. Mặc định: "Tất cả".<br>- **Định dạng option:** [Mã KCN] - [Tên KCN] (VD: "KCN-001 - KCN tái định cư 06").<br>- **Searchable dropdown**: Cho phép tìm kiếm KCN (tìm kiếm gần đúng theo cả mã và tên, sắp xếp A-Z). Chi tiết xem CMR-03.<br><br>**Quy tắc hành động:**<br>- Tap → Mở danh sách lựa chọn (có ô search) → Nhập từ khóa để lọc option → Tap item → Tự động đóng và hiển thị giá trị đã chọn.<br>- Nếu đang ở trạng thái clear (hiển thị placeholder) mà người dùng tap ra ngoài → tự động chọn lại "Tất cả".               |
| 4 | Ngày ký hợp đồng (Từ) | DatePicker                            | Placeholder: "Từ ngày"    | x            | -         | **Quy tắc hiển thị:**<br>- Placeholder mặc định là "Từ ngày".<br>- Hiển thị DatePicker format DD/MM/YYYY theo CMR-12.<br>- Nếu để trống: không lọc.<br><br>**Quy tắc hành động:**<br>- Chọn ngày bắt đầu.<br>- Nếu chỉ chọn ngày bắt đầu, không chọn ngày kết thúc + Ấn Áp dụng → Ngày kết thúc = vô hạn (lọc từ ngày bắt đầu đến hiện tại). (Xem CMR-15)<br><br>**Quy tắc validation:**<br>- Không có.                                                                                                                                                                                                                                                                                                                                            |
| 5 | Ngày ký hợp đồng (Đến) | DatePicker                            | Placeholder: "Đến ngày"  | x            | -         | **Quy tắc hiển thị:**<br>- Placeholder mặc định là "Đến ngày".<br>- Hiển thị DatePicker format DD/MM/YYYY theo CMR-12.<br>- Nếu để trống: không lọc.<br><br>**Quy tắc hành động:**<br>- Chọn ngày kết thúc.<br>- Nếu chỉ chọn ngày kết thúc, không chọn ngày bắt đầu + Ấn Áp dụng → Ngày bắt đầu = không giới hạn (lọc từ đầu đến ngày kết thúc). (Xem CMR-15)<br><br>**Quy tắc validation:**<br>- Khi đã chọn ngày bắt đầu (Từ) → Chỉ cho phép chọn ngày kết thúc từ ngày bắt đầu trở về sau (các ngày trước đó bị disable trong DatePicker). (Xem CMR-15)                                                                                                                                                                 |
| 6 | Ngày kết thúc hợp đồng (Từ) | DatePicker                      | Placeholder: "Từ ngày"    | x            | -         | **Quy tắc hiển thị:**<br>- Placeholder mặc định là "Từ ngày".<br>- Hiển thị DatePicker format DD/MM/YYYY theo CMR-12.<br>- Nếu để trống: không lọc.<br><br>**Quy tắc hành động:**<br>- Chọn ngày bắt đầu.<br>- Nếu chỉ chọn ngày bắt đầu, không chọn ngày kết thúc + Ấn Áp dụng → Ngày kết thúc = vô hạn (lọc từ ngày bắt đầu đến hiện tại). (Xem CMR-15)<br><br>**Quy tắc validation:**<br>- Không có.                                                                                                                                                                                                                                                                                                                                            |
| 7 | Ngày kết thúc hợp đồng (Đến) | DatePicker                      | Placeholder: "Đến ngày"  | x            | -         | **Quy tắc hiển thị:**<br>- Placeholder mặc định là "Đến ngày".<br>- Hiển thị DatePicker format DD/MM/YYYY theo CMR-12.<br>- Nếu để trống: không lọc.<br><br>**Quy tắc hành động:**<br>- Chọn ngày kết thúc.<br>- Nếu chỉ chọn ngày kết thúc, không chọn ngày bắt đầu + Ấn Áp dụng → Ngày bắt đầu = không giới hạn (lọc từ đầu đến ngày kết thúc). (Xem CMR-15)<br><br>**Quy tắc validation:**<br>- Khi đã chọn ngày bắt đầu (Từ) → Chỉ cho phép chọn ngày kết thúc từ ngày bắt đầu trở về sau (các ngày trước đó bị disable trong DatePicker). (Xem CMR-15)                                                                                                                                                                 |
| 8 | Nút "Nhập lại"       | Button (Secondary)                      | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Không đóng Bottom Sheet.<br><br>**Quy tắc hành động:**<br>- Tap → Reset toàn bộ tiêu chí lọc về giá trị mặc định.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 9 | Nút "Áp dụng"        | Button (Primary)                        | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Luôn **Enabled** (vì DatePicker đã disable ngày không hợp lệ theo CMR-15, user không thể chọn sai).<br><br>**Quy tắc hành động:**<br>- Tap → Áp dụng toàn bộ tiêu chí lọc hiện tại, đóng Bottom Sheet, gọi API với tham số bộ lọc, tải lại danh sách hợp đồng. |
| 10 | Nút "X" đóng         | Button (Icon)                           | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Icon "X" nằm ở góc phải trên cùng của Bottom Sheet.<br><br>**Quy tắc hành động:**<br>- Tap → Đóng Bottom Sheet, không thay đổi kết quả hiện tại (tương tự tap vùng ngoài).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

**Khung Danh sách (Card List):**

> Mỗi card đại diện cho một hợp đồng cho thuê đất. Danh sách sắp xếp mặc định theo ngày ký hợp đồng giảm dần.

| # | Tên trường           | Kiểu trường  | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                            |
| - | ----------------------- | --------------- | --------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Số hợp đồng          | Label (Bold, Color) | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Số hợp đồng (VD: "HD02").<br>- Chữ đậm, màu đỏ đặc trưng.<br>- Hiển thị tối đa 2 dòng, quá dài sẽ có dấu ... ở cuối (truncate).                                                                                         |
| 2 | Icon mũi tên (>)      | Icon            | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Chỉ báo cho hành động tap vào card. Hiển thị ở góc phải trên cùng ngang hàng Số hợp đồng.                                                                                                                                                     |
| 3 | Tình trạng | Badge           | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Hiển thị trạng thái hợp đồng (VD: "Đang cho thuê", "Hết hạn", "Thu hồi", "Khác").<br>- **Đang cho thuê**: Badge nền màu xanh dương nhạt, chữ màu xanh dương, viền bo tròn.<br>- Trạng thái khác: theo màu quy định hệ thống.                                                                           |
| 4 | Tên lô                | Label           | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Tên lô đất (VD: "N101").<br>- **Layout:** Label bên trái, value căn phải.<br>- Không có icon ở prefix.<br>- Hiển thị tối đa 2 dòng, quá dài sẽ có dấu ... ở cuối (truncate). |
| 5 | Diện tích             | Label           | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Diện tích (đơn vị m²). Cho phép giá trị **số thập phân**.<br>- **Layout:** Label bên trái, value căn phải.<br>- Định dạng số: 3 chữ số phần nguyên phân cách bằng dấu phẩy (,), phần thập phân phân cách bằng dấu chấm (.) (VD: "2,000.5", "1,500.25"). Áp dụng CMR-11.<br>- Không có icon ở prefix.              |
| 6 | Ngày hiệu lực        | Label + Icon    | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Kèm icon Lịch ở trước Label.<br>- Format ngày tháng: DD/MM/YYYY - DD/MM/YYYY (VD: "30/04/2026 - 30/04/2027").<br>- Value nằm ở dòng dưới label.                                                                        |
| 7 | Ngày ký hợp đồng    | Label           | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Ngày ký hợp đồng. Format DD/MM/YYYY.<br>- **Layout:** Label bên trái, value căn phải.                                                                        |
| 8 | Card hợp đồng         | Card            | -                    | —           | -         | **Quy tắc hành động:**<br>- Tap bất kỳ vị trí nào trên card → mở màn hình Chi tiết thông tin cho thuê đất.<br>- Debounce navigation theo CMR-18: khi người dùng tap nhanh liên tục (double tap) vào card, hệ thống có cơ chế debounce để chỉ trigger 1 lần mở chi tiết, tránh mở trùng lặp màn hình.                                                                                                                                                                         |

**Quy tắc State Persistence (Lưu trạng thái):**

> Sau khi tìm kiếm/lọc/scroll danh sách, nếu người dùng vào màn chi tiết và quay lại, hệ thống phải giữ nguyên:
>
> - Keyword tìm kiếm
> - Filter
> - Vị trí scroll
> - Dữ liệu đã load trước đó
>
> (Xem CMR-01: không reset về trạng thái mặc định.)

---

#### 2.2 Giao diện Chi tiết thông tin cho thuê đất

**Mô tả giao diện:**
Màn hình tiêu đề "Chi tiết thông tin cho thuê đất". Hiển thị thông tin chi tiết của hợp đồng được chọn từ danh sách. **Toàn bộ màn là read-only** (không có input form).

---

**2.2.1 Header:**

| # | Tên trường  | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                        |
| - | -------------- | -------------- | --------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nút quay lại | Button (Icon)  | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Icon ← nằm góc trái header.<br>- Luôn hiển thị trên mọi màn chi tiết. (Xem CMR-06)<br><br>**Quy tắc hành động:**<br>- Tap → Quay về màn danh sách, giữ nguyên trạng thái tìm kiếm/lọc trước đó. |
| 2 | Tiêu đề     | Label          | "Chi tiết thông tin cho thuê đất" | -           | —         | **Quy tắc hiển thị:**<br>- Hiển thị text "Chi tiết thông tin cho thuê đất".<br>- Căn giữa header.<br><br>**Quy tắc hành động:**<br>- Không tap được.                                                                                                     |

---

**2.2.2 Thông tin lô đất:**

| # | Tên trường     | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                  |
| - | ----------------- | -------------- | --------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Khu công nghiệp | Label          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Hiển thị dạng: [Mã KCN] - [Tên KCN] (VD: "KCN-001 - KCN tái định cư 06").<br>- Dữ liệu lấy từ API.<br>- Nếu null → hiển thị "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không cho phép tap.         |
| 2 | Lô đất    | Label (Bold/Red)   | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Tên lô đất (VD: "N101"). Text màu đỏ.<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không tap được.                                                         |
| 3 | Vị trí          | Label          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Vị trí lô đất (VD: "Vị trí 02").<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không tap được.                                                    |
| 4 | Tổng diện tích       | Label (Number) | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Diện tích tổng (đơn vị m²). Cho phép giá trị **số thập phân**.<br>- Định dạng số theo CMR-11.<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không tap được. |
| 5 | Nhà đầu tư thuê đất  | Label          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Tên nhà đầu tư (VD: "Chủ 02").<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không tap được.                                                     |

---

**2.2.3 Thông tin hợp đồng:**

| # | Tên trường          | Kiểu trường       | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                 |
| - | ---------------------- | -------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Số hợp đồng  | Label (Red) | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Số hợp đồng (VD: "HD02"). Text màu đỏ.<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không cho phép tap. |
| 2 | Ngày ký hợp đồng    | Label | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Hiển thị ngày ký format DD/MM/YYYY.<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không cho phép tap.                          |
| 3 | Thời gian hiệu lực    | Label | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Format: Từ ngày -> Đến ngày (VD: "30/04/2026 -> 30/04/2027").<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không cho phép tap.                          |
| 4 | Mục đích thuê | Label | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Mục đích (VD: "Sản xuất kinh doanh").<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không cho phép tap.                         |
| 5 | Tình trạng  | Badge          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- **Đang cho thuê**: Badge nền xanh dương nhạt, chữ xanh dương, có viền bo tròn.<br>- Trạng thái khác: theo hệ thống.<br>- Nếu null → không hiển thị.<br><br>**Quy tắc hành động:**<br>- Không cho phép tap. |

---

**2.2.4 Thông tin tài chính:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                  |
| - | ------------- | -------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Đơn giá thuê trước VAT | Label          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Đơn giá thuê.<br>- Format số theo CMR-11 (VD: "200,000,000").<br>- Nếu null → "-".<br><br>**Quy tắc hành động:**<br>- Không cho phép tap. |
| 2 | VAT | Label          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Tỷ lệ phần trăm (VD: "10%").<br>- Nếu null → "-".<br><br>**Quy tắc hành động:**<br>- Không cho phép tap. |
| 3 | Đơn giá sau VAT | Label (Red)          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Đơn giá sau VAT. Text màu đỏ.<br>- Format số theo CMR-11 (VD: "220,000,000").<br>- Nếu null → "-".<br><br>**Quy tắc hành động:**<br>- Không cho phép tap. |
| 4 | Kỳ thanh toán | Label          | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Hiển thị kỳ thanh toán (VD: "Hằng tháng", "Hằng quý", "Hằng năm").<br>- Nếu null → "-".<br><br>**Quy tắc hành động:**<br>- Không cho phép tap. |

---

**2.2.5 Thông tin bổ sung:**

| # | Tên trường       | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                      |
| - | ------------------- | -------------- | --------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Ghi chú | Label (Multi-line) | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Thông tin ghi chú bổ sung.<br>- Nếu null → "-".<br>- Nếu dài quá → xuống dòng (wrap text), không truncate.<br><br>**Quy tắc hành động:**<br>- Không tap được. |

---

**2.2.6 Tệp đính kèm:**

| # | Tên trường    | Kiểu trường      | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------- | ------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | File đính kèm | List (Icon + Label) | -                    | —           | -         | **Quy tắc hiển thị:**<br>- Hiển thị danh sách file đính kèm hợp đồng. Không giới hạn số lượng file.<br>- Mỗi file gồm icon + tên file.<br>- Tên dài → truncate với dấu "...".<br>- **Thứ tự sắp xếp:** Sắp xếp theo **ngày upload giảm dần** (mới nhất hiển thị trên cùng). Nếu nhiều file được upload cùng lúc → hiển thị theo thứ tự như lúc tạo/chỉnh sửa.<br>- Không có file → hiển thị empty state *"Không có dữ liệu."* (Xem CMR-14).<br><br>**Quy tắc hành động (Xem CMR-08):**<br>- Tap vào file → Hệ thống xử lý theo định dạng:<br>  - **Xem trực tiếp:** PDF, Hình ảnh (JPG, PNG), Video (MP4, AVI, MOV) → Mở xem trực tiếp trên trình duyệt thiết bị.<br>  - **Tải xuống:** Các định dạng khác (DOC, DOCX, XLS, XLSX, ZIP, v.v.) → Tự động tải xuống máy (download).<br>  - **Không hỗ trợ:** Nếu định dạng không hỗ trợ → hiển thị thông báo *"Định dạng không hỗ trợ. Vui lòng tải xuống."*<br><br>**Quy tắc validation:**<br>- File phải có URL hợp lệ. |

---

### 3. Mô tả xử lý

**3.1 Load dữ liệu:**

1. Người dùng tap vào card hợp đồng từ màn Danh sách (2.1).
2. Hệ thống gọi API lấy chi tiết hợp đồng theo ID.
3. Trong khi chờ API phản hồi, hiển thị loading indicator (spinner/skeleton) trên toàn bộ nội dung (Xem CMR-07).
4. **Quy định thời gian phản hồi:** Tối đa 10 giây cho API chi tiết. Quá 10 giây → Hiển thị "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." kèm nút "Thử lại".

**3.2 Mapping dữ liệu:**

1. Map dữ liệu từ API vào các trường UI tương ứng.
2. Nếu giá trị là null → Hiển thị "-".
3. Badge trạng thái map theo value.

**3.3 Xử lý lỗi (Xem CMR-07):**

| Quy tắc       | Mô tả                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lỗi mạng     | Hiển thị thông báo: *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* Kèm nút "Thử lại".                                        |
| Lỗi API (500) | Hiển thị thông báo: *"Hệ thống đang bận. Vui lòng thử lại sau."*                                                                               |
| Lỗi 404       | Hiển thị: *"Nội dung không tồn tại hoặc đã bị xóa."*                                                                                           |
| Lỗi 401 (Session hết hạn) | Hệ thống sẽ tự động sử dụng **refresh token** để cấp lại access token mới. Nếu refresh token đã hết hạn hoặc không hợp lệ (quá **15 ngày**), người dùng sẽ được chuyển về **màn hình đăng nhập** và hiển thị **toast**: *"Phiên đăng nhập hết hạn."* |
| Timeout        | Nếu API không phản hồi trong **10 giây** → Hiển thị thông báo: *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* Kèm nút "Thử lại". |
| Loading state  | Mọi API call phải có loading indicator trong khi chờ kết quả. Đối với **first-load** màn hình danh sách hoặc chi tiết, sử dụng **loading state toàn màn hình** (full-screen loading overlay). Các lần tải tiếp theo (lazy load, refresh) sử dụng loading indicator cục bộ (spinner). |

**3.4 Xử lý Partial Load (Một phần dữ liệu fail):**

- **Không block toàn màn.** Hiển thị partial: phần dữ liệu đã load thành công vẫn hiển thị bình thường; phần bị lỗi hiển thị trạng thái lỗi cục bộ.

---

### 4. Ghi chú

- **Toàn bộ màn là read-only** — không có input form.
- Không có hành động chỉnh sửa trên màn hình này.

---

### 5. Mô tả các xử lý của chức năng

#### 5.1 Xử lý Tải danh sách hợp đồng

1. Người dùng truy cập từ Sidebar → "Thông tin cho thuê đất".
2. Hệ thống gọi API lấy toàn bộ danh sách hợp đồng (không áp dụng bộ lọc).
3. Danh sách hiển thị dạng Card, sắp xếp mặc định theo ngày ký giảm dần.
4. Danh sách hỗ trợ **lazy load** theo CMR-04: tải **20 bản ghi** mỗi lần. Khi người dùng cuộn đến cuối danh sách → tự động tải trang tiếp theo. Hiện loading indicator ở cuối danh sách khi đang tải. Khi hết dữ liệu, ẩn loading indicator và không gọi API nữa. Danh sách rỗng → hiển thị *"Không có dữ liệu."* ở giữa vùng nội dung (Xem CMR-14). Không có action Thử lại vì không phải lỗi.
5. **Quy định thời gian phản hồi:** Tối đa 10 giây cho API load danh sách. Quá 10 giây → Hiển thị "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." kèm nút "Thử lại".

**Xử lý trường hợp rỗng:**

- Nếu không có dữ liệu trong hệ thống: Hiển thị *"Không có dữ liệu."* ở giữa vùng nội dung.

#### 5.2 Xử lý Tìm kiếm & Lọc

1. **Tìm kiếm:** Người dùng nhập từ khóa vào ô tìm kiếm.
   - Debounce 3 giây: hiển thị kết quả tìm kiếm trong lúc gõ, sau 3 giây không gõ mới thực hiện tìm kiếm API.
   - Hệ thống tìm kiếm like theo số hợp đồng và tên lô đất.
   - Tìm kiếm gần đúng (chứa từ khóa). Khi xóa hết từ khóa, danh sách trở về trạng thái mặc định (hiển thị tất cả).
   - **Quy định thời gian phản hồi:** Tối đa 10 giây.
2. **Bộ lọc:** Người dùng tap icon Lọc → Chỉnh sửa tiêu chí trong Bottom Sheet → Tap "Áp dụng".
3. Hệ thống **kết hợp** tham số tìm kiếm và bộ lọc vào một lần gọi API duy nhất.
4. Nếu không có kết quả phù hợp: Hiển thị *"Không tìm thấy kết quả."* ở giữa vùng nội dung.

**Xử lý validate bộ lọc Date (Xem CMR-15):**

- Khi người dùng chọn ngày bắt đầu (Từ) → DatePicker ngày kết thúc (Đến) chỉ cho phép chọn từ ngày bắt đầu trở về sau (các ngày trước đó bị disable).
- Nếu chỉ chọn ngày bắt đầu, không chọn ngày kết thúc → Lọc từ ngày bắt đầu đến hiện tại.
- Nếu chỉ chọn ngày kết thúc, không chọn ngày bắt đầu → Lọc từ đầu đến ngày kết thúc.

**Quy tắc State Persistence:**

- Sau khi tìm kiếm/lọc, nếu người dùng vào màn chi tiết và quay lại, danh sách phải giữ nguyên trạng thái tìm kiếm/lọc/scroll trước đó (không reset về trạng thái mặc định). (Xem CMR-01)

#### 5.3 Pull-to-Refresh

- Màn hình Danh sách hỗ trợ **Pull-to-Refresh**: Người dùng kéo xuống từ đầu danh sách → Hệ thống reload toàn bộ dữ liệu từ đầu (áp dụng bộ lọc & từ khóa tìm kiếm hiện tại).
- Hiển thị spinner/animation ở đầu danh sách trong khi đang refresh.
- Nếu refresh thất bại: Giữ nguyên dữ liệu cũ, hiển thị thông báo lỗi (Xem CMR-07).
- Khi đang pull-to-refresh hoặc lazy load, không trigger lại API tương tự. (Xem CMR-13)

#### 5.4 Đa ngôn ngữ (Multi-language)

- Toàn bộ **text cứng** của màn hình tuân theo ngôn ngữ đang được chọn trong thiết lập ứng dụng.
- **Nội dung dữ liệu** lấy từ API **không thay đổi** theo ngôn ngữ. (Xem CMR-17)

#### 5.5 Debounce Navigation & Khôi phục trạng thái khi mở lại app

- Khi người dùng tap nhanh liên tục (double tap) vào card lô đất hoặc các nút navigation (Quay lại, Lọc...), hệ thống áp dụng cơ chế debounce để tránh mở trùng lặp màn hình.
- **Force close app** (tắt app / Kill app) → Khi mở lại: hệ thống **xóa session đăng nhập**, yêu cầu người dùng **đăng nhập lại từ đầu**. (Xem CMR-18)
- **Uninstall app** → Khi cài lại: yêu cầu đăng nhập lại từ đầu. (Xem CMR-18)

---

## 6. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 16/05/2026 | v1.0 | Khởi tạo tài liệu | (Không có) | Tạo đặc tả UC41 — Tra cứu thông tin cho thuê đất trong KCN trên Mobile: danh sách, bộ lọc, chi tiết | Phiên bản đầu tiên theo system_init_workflow |
| 16/05/2026 | v1.0 → v1.1 | Section 1 — Truy cập chức năng (Sidebar) | "Quản lý cho thuê đất" | "Thông tin cho thuê đất" | BA feedback đổi tên Sidebar |
| 16/05/2026 | v1.0 → v1.1 | Section 2.1 — Header màn list | "Quản lý cho thuê đất" | "Thông tin cho thuê đất" | BA feedback đổi header |
| 16/05/2026 | v1.0 → v1.1 | Section 2.1 — Bộ lọc Tình trạng hợp đồng (options) | "Đang cho thuê / Khác (và các trạng thái khác lấy từ API)" | "Đang cho thuê / Hết hạn / Thu hồi / Khác" | BA xác nhận danh sách trạng thái cố định |
| 16/05/2026 | v1.0 → v1.1 | Section 2.1 — Bộ lọc KCN (định dạng option) | (Không quy định) | Định dạng option: [Mã KCN] - [Tên KCN] (VD: "KCN-001 - KCN tái định cư 06") | BA feedback hiển thị option dropdown |
| 16/05/2026 | v1.0 → v1.1 | Section 2.1 — Card list (Tình trạng hợp đồng) | "Tình trạng hợp đồng" | "Tình trạng" | BA feedback rút gọn label trên card |
| 16/05/2026 | v1.0 → v1.1 | Section 2.1 — Card list (Thời gian thuê) | "Thời gian thuê" — Format "Từ ngày -> Đến ngày" | "Ngày hiệu lực" — Format DD/MM/YYYY - DD/MM/YYYY | BA feedback đổi label & format |
| 16/05/2026 | v1.0 → v1.1 | Section 2.1 — Card list (Ngày ký) | "Ngày ký" | "Ngày ký hợp đồng" | BA feedback đổi label đầy đủ |
| 16/05/2026 | v1.0 → v1.1 | Section 2.2.2 — Khu công nghiệp (định dạng) | Tên khu công nghiệp (VD: "KCN tái định cư 06") | [Mã KCN] - [Tên KCN] (VD: "KCN-001 - KCN tái định cư 06") | BA feedback đồng bộ định dạng với filter |
| 16/05/2026 | v1.0 → v1.1 | Section 2.2.4 — Đơn giá thuê trước VAT & Đơn giá sau VAT | "(đơn vị VNĐ)" + format kèm "VNĐ" (VD: "200.000.000 VNĐ") | Bỏ đơn vị tiền tệ; chỉ format số theo CMR-11 (VD: "200,000,000") | BA feedback bỏ đơn vị tiền tệ |
| 16/05/2026 | v1.0 → v1.1 | Section 2.2.4 — Kỳ thanh toán (mô tả & ví dụ) | "Text kỳ (VD: 'Hàng tháng')" | "Hiển thị kỳ thanh toán (VD: 'Hằng tháng', 'Hằng quý', 'Hằng năm')" | BA feedback bổ sung ví dụ |
| 19/05/2026 | v1.1 → v1.2 | Section 1 — Thêm Phạm vi ngoài (Out-of-scope) | (Không có) | Thêm mục Out-of-scope: không tạo/sửa/xóa thông tin cho thuê đất, không export, không in | BA feedback làm rõ phạm vi chức năng |
| 19/05/2026 | v1.1 → v1.2 | Section 2.2.3 — Thêm quy tắc wrap text | Các fields (Số HĐ, Ngày ký, Thời gian hiệu lực, Mục đích thuê) không có quy tắc "Nếu dài quá" | Thêm: "Nếu dài quá → xuống dòng (wrap text), không truncate" cho tất cả fields | BA feedback bổ sung quy tắc hiển thị |
| 19/05/2026 | v1.1 → v1.2 | Section 3.3 — Xử lý lỗi | Mô tả chung: "Nếu API lỗi: hiển thị thông báo lỗi kèm nút Thử lại" | Bê nguyên bảng CMR-07 vào: tách rõ Lỗi mạng, Lỗi 500, Lỗi 404, Lỗi 401, Timeout, Loading state | BA feedback mô tả đủ case lỗi |
| 19/05/2026 | v1.2 → v1.3 | Section 2.1 — Bộ lọc Date (rows 4-7) | Validation bằng inline error message "Đến phải >= Từ"; không mô tả case chỉ chọn 1 ngày | Đồng bộ CMR-15: disable ngày không hợp lệ trong DatePicker; bổ sung rule chỉ chọn Từ/Đến | QC feedback — đồng bộ CMR-15 |
| 19/05/2026 | v1.2 → v1.3 | Section 2.1 — Nút "Áp dụng" (row 9) | "Disabled khi validation Ngày (Đến < Từ) fail" | "Luôn Enabled (vì DatePicker đã disable ngày không hợp lệ theo CMR-15)" | QC feedback — đồng bộ CMR-15 |
| 19/05/2026 | v1.2 → v1.3 | Section 5.2 — Xử lý validate bộ lọc Date | "Nếu Đến < Từ: hiển thị lỗi inline và không cho tap Áp dụng" | Đồng bộ CMR-15: disable ngày trong DatePicker; chỉ chọn Từ → lọc đến hiện tại; chỉ chọn Đến → lọc từ đầu | QC feedback — đồng bộ CMR-15 |
| 19/05/2026 | v1.3 → v1.4 | Section 2.1 — Giá trị mặc định dropdown (rows 1-3) | "Tất cả nhà đầu tư thuê đất" / "Tất cả tình trạng hợp đồng" / "Tất cả khu công nghiệp" | "Tất cả" cho tất cả dropdown filter | BA feedback — rút gọn giá trị mặc định |
| 20/05/2026 | v1.4 → v1.5 | Section 2.1 — Placeholder dropdown Searchable (rows 1, 3) | (Không có placeholder) | Thêm Placeholder: "Chọn nhà đầu tư thuê đất" (row 1), "Chọn khu công nghiệp" (row 3) | BA feedback — thêm placeholder cho dropdown searchable |
| 20/05/2026 | v1.5 → v1.6 | Section 2.1 — Dropdown Searchable (rows 1, 3): hành vi clear | (Không có) | Hiển thị placeholder khi option được clear; nếu đang clear mà tap ra ngoài → auto chọn lại "Tất cả" | BA feedback — bổ sung hành vi clear/focus-out |
| 2026-05-21 | v1.6 → v1.7 | Align CMR Mobile v6.0 | Search box max length 500→255. |
| 2026-05-22 | v1.7 → v1.8 | Section 2.1 — Placeholder Date (rows 4-7) | Placeholder "Từ" / "Đến" | Placeholder "Từ ngày" / "Đến ngày" | Đồng bộ placeholder date range filter theo chuẩn chung |
| 2026-05-22 | v1.8 → v1.9 | Section 5.5 — Force close app | "giữ nguyên session đăng nhập, app quay về Trang chủ (không yêu cầu đăng nhập lại)" | "xóa session đăng nhập, yêu cầu người dùng đăng nhập lại từ đầu" | Đồng bộ CMR-18 |
