# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC45-51 — Quản lý hồ sơ trên Mobile
**Ngày tạo:** 29/04/2026

| Thuộc tính              | Giá trị                                 |
| ------------------------- | ----------------------------------------- |
| BA phụ trách            | han.luong & huy.lai2                      |
| Phân hệ                 | Ứng dụng Di động (Mobile App)         |
| Loại chức năng         | Quản lý hồ sơ                         |
| Đối tượng thực hiện | Cá nhân / Tổ chức (đã đăng nhập) |
| Giao diện                | Màn hình Mobile (Portrait)              |
| Ngày tạo                | 29/04/2026                                |
| Phiên bản               | v3.2                                      |

---

## UC45-51 — Quản lý hồ sơ trên Mobile

### 1. Mô tả chức năng

**Tên chức năng:** Xem danh sách hồ sơ trên Mobile
**Mô tả:** Chức năng cho phép người dùng xem danh sách toàn bộ hồ sơ đã nộp, tra cứu theo trạng thái và xem chi tiết hồ sơ. Hệ thống hiển thị hồ sơ được phân loại theo các tab trạng thái.
**Phân quyền:** Cá nhân/Tổ chức đã đăng nhập chỉ xem được hồ sơ của chính mình nộp.
**Truy cập chức năng:** Sidebar → "Quản lý hồ sơ".
**Chức năng đáp ứng usecase số:** UC45, UC46, UC47, UC48, UC49, UC50, UC51 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Giao diện Danh sách hồ sơ

**Mô tả giao diện:**
Màn hình cuộn dọc bao gồm các thành phần từ trên xuống dưới: Header đỏ có nút quay lại → Thanh Tab trạng thái (6 tab) → Thanh tìm kiếm và bộ lọc → Danh sách Card hồ sơ.

**Khung Header:**

| # | Tên trường       | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                       |
| - | ------------------- | -------------- | --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------- |
| 1 | Nút Quay lại (←) | Button (Icon)  | —                    | —           | —         | **Quy tắc hành động:** Tap → Quay về màn hình trước đó. (Xem CMR-06) |
| 2 | Tiêu đề Header   | Label          | "Quản lý hồ sơ"   | —           | —         | **Quy tắc hiển thị:** Màu trắng trên nền đỏ đậm, căn giữa.          |

**Quy tắc chung cho Search/Filter & State Persistence:**

- Ô tìm kiếm và bộ lọc nằm **dưới thanh Tab**, áp dụng riêng cho từng tab (không phải toàn cục).
- Mỗi tab lưu trữ **riêng biệt** trạng thái search/filter của mình. Khi chuyển tab A → tab B → quay lại tab A, search/filter của tab A vẫn được **giữ nguyên**.
- Khi người dùng đang search/filter và tap vào card để xem chi tiết, sau đó quay lại → **Giữ nguyên** search/filter (theo CMR-01).
- Chỉ reset search/filter khi người dùng chuyển sang màn hình khác hoàn toàn (qua Sidebar, Footer tab, hoặc điều hướng chính — không bao gồm màn hình chi tiết).

**Debounce Navigation (CMR-18):** Khi người dùng tap nhanh liên tục (double tap) vào card hồ sơ hoặc các button navigation (Back, Filter, Submit), hệ thống chỉ nhận action đầu tiên, chờ thực hiện xong trước khi nhận action tiếp theo.

**Filter Active Indicator (CMR-02):** Khi có bộ lọc đang active (giá trị khác mặc định), hiển thị icon indicator màu xanh lá cây ở góc phải bên trên của icon filter. Khi không có filter active → ẩn indicator.

**Khung Tabs Trạng thái (Horizontal Scroll):**

| # | Tên Tab              | Trạng thái hiển thị trong tab                                                                                                          | Trạng thái active                                |
| - | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| 1 | Tất cả              | Hiển thị toàn bộ hồ sơ không phân biệt trạng thái.                                                                                  | Text/màu đỏ + underline đỏ khi được chọn. |
| 2 | Chờ tiếp nhận       | Chờ tiếp nhận                                                                                                                          | Text/màu đỏ + underline đỏ khi được chọn. |
| 3 | Yêu cầu bổ sung     | Chờ bổ sung                                                                                                                            | Text/màu đỏ + underline đỏ khi được chọn. |
| 4 | Đã tiếp nhận        | Đang xử lý, Yêu cầu dừng xử lý, Đã dừng xử lý, Yêu cầu rút/hủy, Chờ trả kết quả, Đơn vị chuyên môn thụ lý, Đang lấy ý kiến, Đang phê duyệt | Text/màu đỏ + underline đỏ khi được chọn. |
| 5 | Từ chối tiếp nhận   | Từ chối tiếp nhận                                                                                                                      | Text/màu đỏ + underline đỏ khi được chọn. |
| 6 | Đã hoàn thành       | Đã trả kết quả, Đã rút, Không đủ điều kiện                                                                                           | Text/màu đỏ + underline đỏ khi được chọn. |

**Quy tắc hành động:** (Xem CMR-02)

- **Single selection:** Chỉ cho phép chọn 1 tab tại một thời điểm.
- Tap vào tab → **Tự động unselect tab hiện tại** (bỏ underline đỏ) → **Select tab mới** (hiển thị underline đỏ).
- Hệ thống gọi API với tham số trạng thái tương ứng và cập nhật danh sách hồ sơ.
- Tab mặc định (khi mở màn hình): Tab "Tất cả".
- Nếu không có hồ sơ cho trạng thái tương ứng → Hiển thị *"Không có dữ liệu."* (Xem CMR-14).

**Khung Tìm kiếm & Lọc (nằm dưới Tabs, áp dụng riêng cho từng tab):**

| # | Tên trường | Kiểu trường       | Giá trị mặc định                  | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------- | -------------------- | -------------------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Ô tìm kiếm | Textbox (Search)     | Placeholder: "Tìm kiếm nhanh theo mã, tên hồ sơ" | x            | —         | **Quy tắc hiển thị:** (Xem CMR-01)<br>- Icon kính lúp nằm bên trái trong ô.<br>- Placeholder: "Tìm kiếm nhanh theo mã, tên hồ sơ".<br>- Max length: **255 ký tự**. Khi nhập đủ 255 ký tự, không cho phép nhập thêm.<br><br>**Quy tắc hành động:** (Xem CMR-01)<br>- Tìm kiếm gần đúng (contains keyword) theo **mã hồ sơ** và **tên hồ sơ**.<br>- Debounce 3 giây: hiển thị kết quả trong lúc gõ, sau 3 giây không gõ thì áp dụng tìm kiếm.<br>- Không cần nhấn Enter hay nhấn nút nào.<br>- Tự động trim space (cắt khoảng trắng hai đầu) trước khi tìm kiếm. Nếu sau trim rỗng → không trigger search, danh sách về mặc định.<br>- Xóa keyword → hiển thị lại toàn bộ danh sách (trạng thái mặc định).<br>- Khi dùng kết hợp với bộ lọc, kết quả phải thỏa **cả hai** điều kiện.<br>- Phạm vi tìm kiếm: Áp dụng cho **tab hiện tại** (chỉ tìm trong danh sách hồ sơ thuộc tab đang chọn).<br>- Không có kết quả → hiển thị *"Không tìm thấy kết quả."* (Xem CMR-14). |
| 2 | Nút "Lọc"   | Button (Icon Filter) | —                                     | —           | —         | **Quy tắc hiển thị:** Nằm bên phải ô tìm kiếm, viền bo tròn, icon bộ lọc.<br><br>**Quy tắc hành động:** (Xem CMR-02)<br>- Tap icon filter → Mở modal/panel bộ lọc.<br>- Tap 'Áp dụng' / 'Tìm' → Đóng bộ lọc, tải lại danh sách với tiêu chí đã chọn.<br>- Tap 'Nhập lại' / 'Đặt lại' → Reset tất cả trường về giá trị mặc định.<br>- Tap vùng ngoài hoặc nút 'X' → Đóng bộ lọc, không thay đổi kết quả hiện tại.                                 |

**Modal Bộ lọc tìm kiếm (Bottom Sheet):**

> Bộ lọc hiển thị dưới dạng Bottom Sheet. Người dùng chỉnh sửa các tiêu chí trong sheet, sau đó tap "Áp dụng" để áp dụng. Bottom Sheet có nút "X" ở góc phải trên cùng để đóng.

| # | Tên trường     | Kiểu trường              | Giá trị mặc định                  | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------- | --------------------------- | -------------------------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Trạng thái      | Dropdown (Multi-selection, Searchable) | Placeholder: "Chọn trạng thái"  | x            | —         | **Quy tắc hiển thị:** (Xem CMR-03)<br>- Placeholder: "Chọn trạng thái". Khi chưa chọn gì → hiển thị placeholder. Khi không chọn trạng thái nào = lọc tất cả (tương đương không áp dụng filter trạng thái).<br>- **Danh sách option (thay đổi theo tab hiện tại):**<br>&nbsp;&nbsp;• Tab Tất cả: Chờ tiếp nhận, Chờ bổ sung, Đang xử lý, Yêu cầu dừng xử lý, Đã dừng xử lý, Yêu cầu rút/hủy, Chờ trả kết quả, Đơn vị chuyên môn thụ lý, Đang lấy ý kiến, Đang phê duyệt, Từ chối tiếp nhận, Đã trả kết quả, Đã rút, Không đủ điều kiện<br>&nbsp;&nbsp;• Tab Chờ tiếp nhận: Chờ tiếp nhận<br>&nbsp;&nbsp;• Tab Yêu cầu bổ sung: Chờ bổ sung<br>&nbsp;&nbsp;• Tab Đã tiếp nhận: Đang xử lý, Yêu cầu dừng xử lý, Đã dừng xử lý, Yêu cầu rút/hủy, Chờ trả kết quả, Đơn vị chuyên môn thụ lý, Đang lấy ý kiến, Đang phê duyệt<br>&nbsp;&nbsp;• Tab Từ chối tiếp nhận: Từ chối tiếp nhận<br>&nbsp;&nbsp;• Tab Đã hoàn thành: Đã trả kết quả, Đã rút, Không đủ điều kiện<br>- Searchable: Cho phép nhập text để tìm kiếm gần đúng trong danh sách option.<br>- **Hiển thị selected:** Mỗi option đã chọn hiển thị dạng tab (chip) có tên option. Nếu quá nhiều option được chọn, hiển thị "..." ở cuối.<br><br>**Quy tắc hành động:**<br>- Tap → Mở danh sách lựa chọn (multi-select).<br>- Tap option đang unselect → select (highlight). Tap option đang select → unselect.<br>- Nhập keyword → lọc option realtime. Nếu không có option nào phù hợp → hiển thị *"Không có dữ liệu."* (Xem CMR-03).<br>- Xóa hết keyword → hiển thị lại placeholder trong ô search của dropdown (CMR-03).<br>- Tap ra ngoài khi keyword trống → giữ nguyên selection hiện tại, đóng dropdown (CMR-03).<br>- Option đã chọn được highlight/bold khi mở dropdown list.<br>- Nếu tên option vượt quá giới hạn ký tự → Tự động cắt ngắn và hiển thị "..." ở cuối. |
| 2 | Ngày tiếp nhận | Date Range Picker           | Placeholder: "Từ ngày - Đến ngày" | x            | —         | **Quy tắc hiển thị:** (Xem CMR-15)<br>- Cho phép chọn khoảng thời gian từ ngày - đến ngày bằng component lịch (calendar picker).<br>- Định dạng ngày hiển thị: DD/MM/YYYY (Xem CMR-12).<br><br>**Quy tắc hành động:**<br>- Tap vào field → Mở calendar popup.<br>- Chỉ chọn ngày bắt đầu, không chọn ngày kết thúc → Ngày kết thúc = vô hạn (lọc từ ngày bắt đầu đến hiện tại).<br>- Chỉ chọn ngày kết thúc, không chọn ngày bắt đầu → Ngày bắt đầu = không giới hạn (lọc từ đầu đến ngày kết thúc).<br>- Khi chọn ngày bắt đầu → Chỉ cho phép chọn ngày kết thúc từ ngày bắt đầu trở về sau (các ngày trước đó bị disable).<br><br>**Quy tắc validation:**<br>- Ngày "Đến ngày" phải lớn hơn hoặc bằng ngày "Từ ngày".<br>- Nếu invalid → Hiển thị inline error: "Ngày kết thúc phải lớn hơn hoặc bằng ngày bắt đầu!" (Xem CMR-15). |
| 3 | Ngày hẹn trả   | Date Range Picker           | Placeholder: "Từ ngày - Đến ngày" | x            | —         | **Quy tắc hiển thị:** (Xem CMR-15)<br>- Cho phép chọn khoảng thời gian từ ngày - đến ngày bằng component lịch (calendar picker).<br>- Định dạng ngày hiển thị: DD/MM/YYYY (Xem CMR-12).<br><br>**Quy tắc hành động:**<br>- Tap vào field → Mở calendar popup.<br>- Chỉ chọn ngày bắt đầu, không chọn ngày kết thúc → Ngày kết thúc = vô hạn (lọc từ ngày bắt đầu đến hiện tại).<br>- Chỉ chọn ngày kết thúc, không chọn ngày bắt đầu → Ngày bắt đầu = không giới hạn (lọc từ đầu đến ngày kết thúc).<br>- Khi chọn ngày bắt đầu → Chỉ cho phép chọn ngày kết thúc từ ngày bắt đầu trở về sau (các ngày trước đó bị disable).<br><br>**Quy tắc validation:**<br>- Ngày "Đến ngày" phải lớn hơn hoặc bằng ngày "Từ ngày".<br>- Nếu invalid → Hiển thị inline error: "Ngày kết thúc phải lớn hơn hoặc bằng ngày bắt đầu!" (Xem CMR-15). |
| 4 | Nút "X" đóng   | Button (Icon)               | —                                     | —           | —         | **Quy tắc hiển thị:** Icon "X" nằm ở góc trên phải của Bottom Sheet. Màu xám đậm, viền bo tròn nếu có nền.<br><br>**Quy tắc hành động:** Tap vùng ngoài hoặc tap nút "X" → Đóng Bottom Sheet, không thay đổi kết quả hiện tại. (Xem CMR-02)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 5 | Nút "Nhập lại" | Button (Secondary)          | —                                     | —           | —         | **Quy tắc hiển thị:** Nút viền outline màu đỏ, text màu đỏ. Không đóng Bottom Sheet.<br><br>**Quy tắc hành động:** (Xem CMR-02)<br>- Tap → Reset toàn bộ tiêu chí lọc về giá trị mặc định.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 6 | Nút "Áp dụng"  | Button (Primary)            | —                                     | —           | —         | **Quy tắc hiển thị:** Nút nền đỏ filled, text trắng.<br><br>**Quy tắc hành động:** (Xem CMR-02)<br>- Tap → Áp dụng toàn bộ tiêu chí lọc hiện tại.<br>- Đóng Bottom Sheet.<br>- Gọi API với tham số bộ lọc và tải lại danh sách hồ sơ.<br>- Nếu không có kết quả phù hợp → hiển thị "Không tìm thấy kết quả." (Xem CMR-14)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

**Quy tắc nút Back vật lý (Android):** Khi Bottom Sheet bộ lọc đang mở, người dùng nhấn nút Back vật lý (Android) → Quay về màn hình trước đó (không chỉ đóng Bottom Sheet).

**Khung Danh sách hồ sơ (Card List):**

> Mỗi card đại diện cho một hồ sơ. Danh sách sắp xếp mặc định theo ngày nộp giảm dần (mới nhất lên đầu).

| # | Tên trường           | Kiểu trường         | Giá trị mặc định | Được sửa | Bắt buôc | Mô tả/Ghi chú                                                                                                                                                                                                                   |
| - | ----------------------- | ---------------------- | --------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Mã hồ sơ & Thủ tục | Label                  | —                    | —           | —         | **Quy tắc hiển thị:** Format: [Mã hồ sơ] • [Mã thủ tục]. Mã hồ sơ hiển thị màu đỏ đậm. Hiển thị tối đa 1 dòng, quá dài sẽ truncate với "..." ở cuối.                                          |
| 2 | Trạng thái            | Badge                  | —                    | —           | —         | **Quy tắc hiển thị:** (Xem CMR-05)<br><br>Màu sắc dựa theo UI design <br><br>**Quy tắc hành động:** Badge trạng thái luôn read-only, không cho phép tap.                                        |
| 3 | Tên thủ tục          | Label (Bold)           | —                    | —           | —         | **Quy tắc hiển thị:** Tên thủ tục đăng ký. Hiển thị tối đa 2 dòng, quá dài sẽ có dấu "..." ở cuối (truncate).                                                                                           |
| 4 | Đơn vị               | Label (Icon Tòa nhà) | —                    | —           | —         | **Quy tắc hiển thị:** Icon tòa nhà (màu xám) + tiền tố "Đơn vị: " + Tên cơ quan. Wrap text nếu dài quá, không truncate.                                                                                    |
| 5 | Người nộp            | Label (Icon Người)   | —                    | —           | —         | **Quy tắc hiển thị:** Icon người (màu xám) + tiền tố "Người nộp: " + Tên người nộp. Wrap text nếu dài quá, không truncate.                                                 |
| 6 | Ngày nộp              | Label (Icon Lịch)     | —                    | —           | —         | **Quy tắc hiển thị:** Icon lịch (màu xám) + tiền tố "Ngày nộp: " + DD/MM/YYYY (Xem CMR-12).                                                                                                                        |
| 7 | Icon Điều hướng (>) | Icon                   | —                    | —           | —         | **Quy tắc hiển thị:** Icon mũi tên ">" màu xám, nằm ở góc phải Card.<br><br>**Quy tắc hành động:** Tap vào bất kỳ đâu trên Card hoặc icon này → Chuyển sang màn hình Chi tiết hồ sơ. |

---

#### 2.2 Giao diện Chi tiết hồ sơ

**Mô tả giao diện:**
Header tiêu đề "Chi tiết hồ sơ", có nút quay lại ←. Nội dung màn hình cuộn dọc chia thành các khối (Section) riêng biệt, hiển thị đầy đủ thông tin chi tiết của hồ sơ. Toàn bộ màn hình là read-only.

**Quy tắc hiển thị chung:** Tất cả các field label trong màn hình chi tiết đều **wrap text nếu dài quá, không truncate**.

**Quy tắc giao diện:** Giao diện chi tiết hồ sơ không có khác biệt giữa người dùng "Cá nhân" và "Tổ chức".

**Khung Header:**

| # | Tên trường       | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                             |
| - | ------------------- | -------------- | --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------- |
| 1 | Nút Quay lại (←) | Button (Icon)  | —                    | —           | —         | **Quy tắc hành động:** Tap → Quay về màn hình Danh sách hồ sơ. (Xem CMR-06) |
| 2 | Tiêu đề Header   | Label          | "Chi tiết hồ sơ"   | —           | —         | **Quy tắc hiển thị:** Màu trắng trên nền đỏ đậm, căn giữa.                |

**Khung Notice Banner (Lý do):**

> Banner thông báo lý do, hiển thị có điều kiện giữa Header và Banner chính. Chỉ xuất hiện khi trạng thái hồ sơ là **Từ chối tiếp nhận** hoặc **Chờ bổ sung**.

| # | Tên trường | Kiểu trường                | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                           |
| - | ------------- | ----------------------------- | --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Lý do       | Alert Banner (Icon + Label) | —                    | —           | —         | **Quy tắc hiển thị:**<br>- Icon cảnh báo (⚠) + tiền tố "Lý do: " + nội dung lý do.<br>- Nền nhạt (light background), viền trái hoặc icon màu cảnh báo theo UI design.<br>- Wrap text nếu dài, không truncate.<br>- Chỉ hiển thị khi trạng thái là **Từ chối tiếp nhận** hoặc **Chờ bổ sung**.<br>- Nếu trạng thái khác hoặc lý do null → Ẩn toàn bộ banner.<br><br>**Quy tắc hành động:** Read-only, không cho phép tap. |

**2.2.1 Banner chính (Nền đỏ):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                            |
| - | ------------- | -------------- | --------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Mã hồ sơ   | Label (Bold)   | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị mã hồ sơ (Size lớn). Wrap text nếu dài, không truncate.                                                    |
| 2 | Trạng thái  | Badge          | —                    | —           | —         | **Quy tắc hiển thị:** Badge trạng thái tương ứng. Màu sắc dựa theo UI design. (Xem CMR-05)                                                 |
| 3 | Ngày nộp    | Label          | —                    | —           | —         | **Quy tắc hiển thị:** Icon lịch + "Ngày nộp: DD/MM/YYYY HH:mm" (Xem CMR-12). Nếu null → hiển thị "-". Wrap text nếu dài, không truncate. |

**2.2.2 Section 1 — Thông tin chung hồ sơ:**

| # | Tên trường                      | Kiểu trường    | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                      |
| - | ---------------------------------- | ----------------- | --------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Tên dịch vụ công               | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị tên dịch vụ công. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".                            |
| 2 | Đối tượng                      | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị đối tượng thực hiện (Cá nhân/Tổ chức). Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-". |
| 3 | Tỉnh/thành                       | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị tên tỉnh/thành. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".                               |
| 4 | Số bộ hồ sơ                    | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị số bộ hồ sơ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".                                 |
| 5 | Số đến                           | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị số đến của hồ sơ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".                       |
| 6 | Số công văn                      | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị số công văn. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".                               |
| 7 | Ngày công văn                    | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị ngày công văn. Định dạng: DD/MM/YYYY (Xem CMR-12).<br>- Nếu null → hiển thị "-".                            |
| 8 | Phí hồ sơ                        | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị phí hồ sơ. Định dạng số theo (Xem CMR-11), luôn kèm đơn vị tiền tệ **VNĐ**. Nếu phí bằng 0 → Hiển thị "0 VNĐ". Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-". |
| 9 | Số ngày kiểm tra hợp lệ       | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị số ngày kiểm tra hợp lệ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-". |
| 10 | Ngày trả lời kiểm tra hợp lệ | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị ngày trả lời kiểm tra hợp lệ. Định dạng: DD/MM/YYYY (Xem CMR-12).<br>- Nếu null → hiển thị "-".  |
| 11 | Số ngày giải quyết             | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị số ngày giải quyết. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".       |
| 12 | Ngày hẹn trả                    | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị ngày hẹn trả. Định dạng: DD/MM/YYYY (Xem CMR-12).<br>- Nếu null → hiển thị "-".  |

**2.2.3 Section 2 — Thông tin tiếp nhận & trả kết quả:**

| # | Tên trường                 | Kiểu trường    | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                          |
| - | ----------------------------- | ----------------- | --------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Phương thức tiếp nhận    | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị phương thức tiếp nhận hồ sơ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-". |
| 2 | Phương thức giao kết quả | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị phương thức giao kết quả. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".      |
| 3 | Ngày tiếp nhận             | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị ngày tiếp nhận hồ sơ. Định dạng: DD/MM/YYYY (Xem CMR-12).<br>- Nếu null → hiển thị "-".          |
| 4 | Thời hạn giải quyết       | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị thời hạn giải quyết hồ sơ. Định dạng: DD/MM/YYYY (Xem CMR-12).<br>- Nếu null → hiển thị "-".    |
| 5 | Đơn vị tiếp nhận         | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị tên đơn vị tiếp nhận hồ sơ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-". |
| 6 | Đơn vị xử lý             | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị tên đơn vị xử lý hồ sơ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".     |

**2.2.4 Section 3 — Nội dung chi tiết:**

| # | Tên trường      | Kiểu trường    | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                          |
| - | ------------------ | ----------------- | --------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Nội dung hồ sơ  | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị nội dung hồ sơ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".                  |
| 2 | Thông tin dự án | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị thông tin dự án (nếu có). Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-".      |
| 3 | Ghi chú           | Label (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị ghi chú (nếu có). Wrap text nếu dài, không truncate.<br>- Nếu không có ghi chú → hiển thị "-". |

**2.2.5 Section 4 — Kết quả & tài liệu:**

| # | Tên trường    | Kiểu trường      | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ---------------- | ------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | File đính kèm | List (Icon + Label) | —                    | —           | —         | **Quy tắc hiển thị:** (Xem CMR-08)<br>- Hiển thị danh sách file đính kèm. Icon file + Tên file + Format file (VD: PDF, DOCX, XLSX).<br>- Tên dài → truncate với dấu "..." ở cuối.<br>- Không có file → hiển thị empty state *"Không có dữ liệu."* (Xem CMR-14).<br><br>**Quy tắc hành động:**<br>- Tap item → Mở viewer/document handler để xem tài liệu.<br>- PDF, Hình ảnh (JPG, PNG), Video (MP4, AVI, MOV) → Mở xem trực tiếp trên trình duyệt thiết bị. Các định dạng khác (DOC, DOCX, XLS, XLSX, ZIP, v.v.) → Tự động tải xuống máy (download). (Xem CMR-08).` |

**2.2.6 Section 5 — Tiến trình xử lý:**

| # | Tên trường | Kiểu trường       | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                      |
| - | ------------- | -------------------- | --------------------- | ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Timeline      | Timeline (Read-only) | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị timeline các bước xử lý (VD: Đã nộp hồ sơ (Ngày giờ), Đang xử lý...). Mỗi bước gồm tên bước + ngày giờ. Wrap text nếu dài, không truncate.<br>- Nếu null → hiển thị "-". |
| 2 | Trạng thái  | Badge                | —                    | —           | —         | **Quy tắc hiển thị:** Badge trạng thái hiện tại của tiến trình. Màu sắc dựa theo UI design. (Xem CMR-05)                                                                                                                           |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Tải danh sách hồ sơ

1. Người dùng truy cập màn hình Quản lý hồ sơ.
2. Hệ thống mặc định hiển thị Tab "Tất cả" và gọi API lấy danh sách.
3. Danh sách sắp xếp theo ngày nộp giảm dần.
4. Hỗ trợ **lazy load** 20 bản ghi/lần. (Xem CMR-04)

**State Persistence:**
- **Giữ tab khi quay lại:** Khi người dùng vào chi tiết hồ sơ và nhấn Back quay lại danh sách, hệ thống giữ nguyên tab đang chọn trước đó (không reset về "Tất cả").
- **Giữ scroll position:** Khi quay lại từ chi tiết, danh sách giữ nguyên vị trí cuộn trước đó.
- **Giữ search/filter:** Trạng thái tìm kiếm và bộ lọc được giữ nguyên khi quay lại từ chi tiết. (Xem CMR-01)

**Loading state:**
- **First-load:** Khi mở màn hình lần đầu hoặc đổi tab, sử dụng loading state toàn màn hình (full-screen loading overlay). (Xem CMR-07)
- **Subsequent load:** Các lần tải tiếp theo (lazy load, refresh) sử dụng loading indicator cục bộ (spinner).

**Lazy load retry:** (Xem CMR-04)
- Khi tải trang N bị lỗi → Hệ thống tự động retry 3 lần (mỗi lần cách nhau ~2 giây).
- Sau 3 lần retry vẫn fail → Dừng tự động retry, hiển thị thông báo lỗi cục bộ ở cuối danh sách.
- Người dùng có thể dùng pull-to-refresh để tải lại từ đầu.

**Pull to refresh:** (Xem CMR-13)

- Kéo xuống từ đầu danh sách → Trigger refresh dữ liệu từ đầu.
- Hiển thị spinner ở đầu danh sách trong khi đang refresh.
- Sau khi refresh thành công: Cập nhật danh sách, ẩn spinner.

**Xử lý lỗi:** (Xem CMR-07)

| Tình huống lỗi           | Thông báo hiển thị                                                                             | Hành vi hệ thống                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Lỗi mạng / Mất kết nối | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + nút **"Thử lại"** | Giữ nguyên màn hình, hiển thị nút Thử lại. Dữ liệu đã load trước đó (qua lazy load) được giữ lại trên màn hình; chỉ hiển thị lỗi cho phần chưa load được. |
| Lỗi API (HTTP 500)         | *"Hệ thống đang bận. Vui lòng thử lại sau."*                                              | Giữ nguyên màn hình, chỉ hiển thị thông báo.            |
| Timeout (quá 10 giây)     | *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + nút **"Thử lại"**       | Giữ nguyên màn hình, hiển thị nút Thử lại. (Xem CMR-16) |
| Session hết hạn (HTTP 401) | Toast: *"Phiên đăng nhập hết hạn."* | Hệ thống tự động sử dụng refresh token để cấp lại access token mới. Nếu refresh token hết hạn hoặc không hợp lệ (quá **15 ngày**) → Redirect về màn hình đăng nhập. (Xem CMR-07) |

**Xử lý lỗi trống (Empty state):** (Xem CMR-14)

- Nếu không có hồ sơ: Hiển thị Empty State (Thông báo *"Không có dữ liệu."*).
- Nếu search/filter không có kết quả: Hiển thị *"Không tìm thấy kết quả."*.

**Xử lý lỗi màn hình Chi tiết (Partial Data):**

- Màn hình chi tiết gọi nhiều endpoint (thông tin chung, file đính kèm, timeline).
- Hiển thị section tải thành công bình thường. Section bị lỗi hiển thị thông báo lỗi riêng theo CMR-07 — không block toàn bộ màn hình.

#### 3.2 Đa ngôn ngữ (→ Xem CMR-17)

Toàn bộ text cứng trên màn hình UC45-51 (header, tên tab trạng thái, placeholder ô tìm kiếm, label bộ lọc, tên trường chi tiết, thông báo lỗi, empty state message, toast) được dịch sang ngôn ngữ hiển thị tương ứng khi người dùng đổi ngôn ngữ. Hỗ trợ 5 ngôn ngữ: VI, EN, ZH, JA, KO. Nội dung dữ liệu từ API (tên hồ sơ, mã hồ sơ, trạng thái, timeline) hiển thị nguyên bản — không thay đổi theo ngôn ngữ.

#### 3.3 Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Danh sách hiển thị đúng 6 tab trạng thái (Tất cả, Chờ tiếp nhận, Yêu cầu bổ sung, Đã tiếp nhận, Từ chối tiếp nhận, Đã hoàn thành) và khớp dữ liệu thực tế.
- **AC2:** Card hồ sơ hiển thị đầy đủ các icon đúng màu sắc thiết kế.
- **AC3:** Toàn bộ card hồ sơ có thể tap để vào màn hình chi tiết.
- **AC4:** Màn hình chi tiết hiển thị đầy đủ 5 section thông tin theo thiết kế.
- **AC5:** Các file đính kèm mở được viewer in-app hoặc ứng dụng hỗ trợ.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-07 | v2 → v2.1 | Bảng Xử lý lỗi — Thêm HTTP 401 | (Không có) | Session hết hạn (HTTP 401): tự động sử dụng refresh token; nếu refresh token hết hạn (>15 ngày) → redirect đăng nhập + toast "Phiên đăng nhập hết hạn" (CMR-07) | Bổ sung xử lý session |
| 2026-05-11 | v2.1 → v2.2 | Đa ngôn ngữ | (Không có) | Bổ sung section đa ngôn ngữ: text cứng dịch 5 ngôn ngữ (VI, EN, ZH, JA, KO), nội dung API giữ nguyên | Đồng bộ CMR-17 (B2) |
| 2026-05-11 | v2.1 → v2.2 | State Persistence | (Không có) | Bổ sung: giữ tab khi quay lại từ chi tiết, giữ scroll position, giữ search/filter | Đồng bộ C4 |
| 2026-05-11 | v2.1 → v2.2 | Loading state | (Không có) | First-load: full-screen loading overlay. Subsequent: spinner cục bộ | Đồng bộ CMR-07 |
| 2026-05-11 | v2.1 → v2.2 | Lazy load retry | (Không có) | Retry tự động 3 lần (mỗi lần cách 2s). Sau 3 lần fail → dừng, hiển thị lỗi cục bộ | Đồng bộ CMR-04 |
| 2026-05-11 | v2.1 → v2.2 | Metadata version fix | Metadata table: v2 | Metadata table: v2.2 (đồng bộ header) | Đồng bộ D1 |
| 2026-05-12 | v2.2 → v2.3 | Bổ sung CMR-18 (Debounce Navigation) | (Không có) | Double-tap debounce trên card và button navigation | Đồng bộ Cross-UC Inconsistency Report v2 |
| 2026-05-12 | v2.2 → v2.3 | Bổ sung Filter Active Indicator (CMR-02) | (Không có) | Icon indicator xanh lá cây khi filter active | Đồng bộ CMR-02 v1.1 |
| 2026-05-12 | v2.2 → v2.3 | Tab switching behavior | Reset search/filter khi chuyển tab | Giữ nguyên search/filter khi chuyển tab nội bộ (chỉ reset khi chuyển màn — không bao gồm màn chi tiết) | Đồng bộ CMR-01 v1.4 |
| 2026-05-12 | v2.3 → v2.4 | Back vật lý Android — Bottom Sheet | (Không có) | Khi Bottom Sheet bộ lọc đang mở, nhấn Back vật lý (Android) → Quay về màn hình trước đó | Feedback BA |
| 2026-05-12 | v2.3 → v2.4 | Partial Data — Màn chi tiết | (Không có) | Hiển thị section tải thành công bình thường. Section bị lỗi hiển thị thông báo lỗi riêng theo CMR-07 — không block toàn bộ màn hình | Feedback BA |
| 2026-05-12 | v2.3 → v2.4 | Ghi chú UI Cá nhân / Tổ chức | (Không có) | Giao diện chi tiết hồ sơ không có khác biệt giữa Cá nhân và Tổ chức | Feedback BA |
| 2026-05-12 | v2.3 → v2.4 | Sửa tham chiếu sorting | Danh sách sắp xếp theo ngày nộp giảm dần (Xem CMR-11) | Danh sách sắp xếp theo ngày nộp giảm dần. (Xóa tham chiếu CMR-11 sai) | Feedback BA |
| 2026-05-12 | v2.3 → v2.4 | Giữ dữ liệu khi mất mạng giữa chừng | Giữ nguyên màn hình, hiển thị nút Thử lại. | Giữ nguyên màn hình + dữ liệu đã load (lazy load) được giữ lại; chỉ hiển thị lỗi cho phần chưa load | Feedback BA |
| 2026-05-12 | v2.3 → v2.4 | Bỏ phiên bản ở title | `**Phiên bản:** v2.4` dưới tiêu đề | (Đã xóa) — chỉ giữ phiên bản trong bảng thuộc tính | Feedback BA |
| 2026-05-15 | v2.4 → v2.5 | Dropdown Trạng thái — Không có kết quả search | (Không có) | Nếu nhập text tìm kiếm mà không có option trùng khớp → Hiển thị "Không có dữ liệu" trong danh sách option (Xem CMR-03) | Đồng bộ CMR-03 v1.6 |
| 2026-05-21 | v2.5 → v2.6 | Align CMR Mobile v6.0 | 1. Khai báo search box max length 255. 2. Bỏ dấu "." trong "Không có dữ liệu" dropdown. 3. Date validation error thêm "!". |
| 2026-05-21 | v2.6 → v2.7 | Dropdown filter | Giá trị mặc định "Tất cả trạng thái"→"Tất cả". Thêm placeholder "Chọn trạng thái" cho searchable dropdown. |
| 2026-05-21 | v2.3 → v2.4 | Clean up incorrect CMR references | Thay các mã tracking bằng CMR-xx chuẩn |
| 2026-05-21 | v2.7 → v2.8 | Tabs Trạng thái | Cập nhật mapping tab↔trạng thái: Tab "Từ chối"→"Từ chối tiếp nhận", "Hoàn thành"→"Đã hoàn thành". Bổ sung chi tiết trạng thái hiển thị trong từng tab (Đang xử lý, Yêu cầu dừng xử lý, Đã dừng xử lý, Yêu cầu rút/hủy, Chờ trả kết quả, Đơn vị chuyên môn thụ lý, Đang lấy ý kiến, Đang phê duyệt, Đã trả kết quả, Đã rút, Không đủ điều kiện, Chờ bổ sung). |
| 2026-05-21 | v2.8 → v2.9 | Cập nhật tổng hợp | 1. Ô tìm kiếm: bổ sung đầy đủ rules theo CMR-01 (max 255, auto-trim, debounce, phạm vi tab, state persistence). 2. Filter Trạng thái: Single→Multi-select, searchable, placeholder "Chọn trạng thái", toggle select/unselect, danh sách 14 trạng thái. 3. Bỏ field "Lý do" khỏi Card List. 4. Chi tiết hồ sơ: gộp Section "Văn bản & pháp lý" + "Tiến độ & thời hạn" vào Section 1 "Thông tin chung". Thêm Ngày tiếp nhận + Thời hạn giải quyết vào Section 2 "Thông tin tiếp nhận & trả kết quả". Xóa Section 6 cũ. Đánh lại số section. |
| 2026-05-21 | v2.9 → v3.0 | Layout & Filter per-tab | 1. Move Tìm kiếm & Lọc xuống dưới Tabs (layout: Header→Tabs→Search/Filter→Card List). 2. Search/Filter áp dụng riêng cho từng tab (không toàn cục). 3. Mỗi tab lưu riêng state search/filter — chuyển tab A→B→A vẫn giữ nguyên. 4. Filter Trạng thái: danh sách option thay đổi theo tab hiện tại. 5. Phạm vi tìm kiếm: chỉ trong tab hiện tại (không phải toàn bộ tab). |
| 2026-05-24 | v3.0 → v3.1 | Card List — Bỏ Badge Cá nhân/Tổ chức | Field Người nộp: "Tên người nộp + Badge [Cá nhân/Tổ chức]" | Field Người nộp: "Tên người nộp" (bỏ Badge) | Yêu cầu BA |
| 2026-05-24 | v3.0 → v3.1 | Section 1 — Bỏ trường Mã hồ sơ | Mã hồ sơ (field #2 trong Section 1) | (Đã xóa) — trùng lặp với Banner 2.2.1 | Đồng bộ design |
| 2026-05-24 | v3.0 → v3.1 | Section 2 — Bỏ trường Ngày nộp | Ngày nộp (field #5 trong Section 2) | (Đã xóa) — trùng lặp với Banner 2.2.1 | Đồng bộ design |
| 2026-05-24 | v3.0 → v3.1 | Section 1 — Sắp xếp lại thứ tự | Thứ tự cũ: Tên DVC, Mã HS, Đối tượng, Tỉnh/thành, Số bộ HS, Số ngày KTHL, Ngày trả lời KTHL, Số ngày GQ, Ngày hẹn trả, Số đến, Số CV, Ngày CV, Phí HS | Thứ tự mới: Tên DVC, Đối tượng, Tỉnh/thành, Số bộ HS, Số đến, Số CV, Ngày CV, Phí HS, Số ngày KTHL, Ngày trả lời KTHL, Số ngày GQ, Ngày hẹn trả | Đồng bộ design |
| 2026-05-24 | v3.0 → v3.1 | Section 2 — Sắp xếp lại thứ tự | Thứ tự cũ: PT tiếp nhận, PT giao KQ, ĐV tiếp nhận, ĐV xử lý, Ngày nộp, Ngày tiếp nhận, Thời hạn GQ | Thứ tự mới: PT tiếp nhận, PT giao KQ, Ngày tiếp nhận, Thời hạn GQ, ĐV tiếp nhận, ĐV xử lý | Đồng bộ design |
| 2026-05-24 | v3.1 → v3.2 | Thêm Notice Banner (Lý do) | (Không có) | Thêm Khung Notice Banner giữa Header và Banner 2.2.1: Alert Banner (Icon ⚠ + "Lý do: " + nội dung). Hiển thị khi trạng thái Từ chối tiếp nhận hoặc Chờ bổ sung. Ẩn khi trạng thái khác/null | Đồng bộ design |
| 2026-05-24 | v3.1 → v3.2 | Section 3 — Bỏ trường Lý do | Lý do (field #3 trong Section 3, hiển thị khi Từ chối/Yêu cầu bổ sung) | (Đã xóa) — chuyển lên Notice Banner, tránh trùng lặp | Đồng bộ design |
